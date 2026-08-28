#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera el sitio estático LlamaLeads Academy a partir de data/rows.json
(volcado de la base de Notion //Llama_Academy).

DISEÑO: nada de nombres de módulo o categoría está hardcodeado.
Todo se agrupa dinámicamente a partir de lo que exista en rows.json:

  Básicos (o cualquier categoría en CATEGORIES_WITH_NIVEL_SPLIT)
      → agrupado por Nivel, y dentro de cada Nivel por Módulo
  Otros Workflows (o cualquier otra categoría futura)
      → agrupado directo por Módulo

Para actualizar el sitio cuando cambian los datos en Notion:
  1. Volver a consultar Notion y sobreescribir data/rows.json
  2. Correr: python3 build.py && python3 shell.py
Nunca hace falta tocar este archivo para agregar módulos/categorías nuevas.
"""
import html
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
ASSETS_DIR = ROOT / "assets"
BUILD_DIR = ROOT / "build"
BUILD_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------
# 1. Cargar datos crudos
# ---------------------------------------------------------------

with open(DATA_DIR / "rows.json", encoding="utf-8") as f:
    ROWS = json.load(f)

NIVEL_META = {
    "inicial":    {"label": "Inicial",    "emoji": "🟢", "badge": "badge-yellow", "accent": "var(--yellow)"},
    "intermedio": {"label": "Intermedio", "emoji": "🔵", "badge": "badge-red",    "accent": "var(--red)"},
    "avanzado":   {"label": "Avanzado",   "emoji": "🟣", "badge": "badge-ink",    "accent": "var(--violet)"},
}
NIVEL_ORDER = ["inicial", "intermedio", "avanzado"]

# Orden preferido de categorías conocidas; cualquier categoría nueva que
# aparezca en Notion y no esté en esta lista se agrega al final automáticamente.
CATEGORY_ORDER_HINT = ["Básicos", "Otros Workflows"]

# Categorías que se organizan por Nivel (además de por Módulo).
# Cualquier categoría que NO esté aquí se agrupa solo por Módulo.
CATEGORIES_WITH_NIVEL_SPLIT = {"Básicos"}


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[\s_]+", "-", s)


def nivel_key(raw):
    """'🟢 Inicial' -> 'inicial' (match tolerante, por si cambia el emoji)."""
    if not raw:
        return "inicial"
    low = raw.lower()
    for key in NIVEL_ORDER:
        if key in low:
            return key
    return "inicial"


def clase_display(code):
    if not code:
        return None
    code = str(code)
    mod, num = code[:-2], code[-2:]
    return f"{mod}.{num}"


def esc(s):
    return html.escape(s) if s else ""

# ---------------------------------------------------------------
# 2. Normalizar filas
# ---------------------------------------------------------------

rows = []
for r in ROWS:
    rows.append({
        "clase": r.get("Clase"),
        "titulo": r.get("Título") or "",
        "desc": r.get("Descripción") or "",
        "modulo": r.get("Módulo") or "Sin módulo",
        "nivel": nivel_key(r.get("Nivel")),
        "categoria": r.get("CATEGORY") or "Sin categoría",
        "video": r.get("VIDEO"),
    })

# ---------------------------------------------------------------
# 3. Agrupar dinámicamente: categoria -> [nivel ->] modulo -> [rows]
# ---------------------------------------------------------------

categorias_presentes = []
for r in rows:
    if r["categoria"] not in categorias_presentes:
        categorias_presentes.append(r["categoria"])
# Orden: primero las conocidas (en el orden del hint), luego las nuevas tal
# como van apareciendo en los datos.
categorias_ordenadas = [c for c in CATEGORY_ORDER_HINT if c in categorias_presentes]
categorias_ordenadas += [c for c in categorias_presentes if c not in categorias_ordenadas]


def group_by_modulo(rows_subset):
    groups = {}
    for r in rows_subset:
        groups.setdefault(r["modulo"], []).append(r)
    return groups


# ---------------------------------------------------------------
# 4. Render de componentes HTML
# ---------------------------------------------------------------

def card_html(r):
    meta = NIVEL_META[r["nivel"]]
    clase_disp = clase_display(r["clase"])
    has_video = bool(r["video"])
    tag = "a" if has_video else "div"
    href_attr = f' href="{esc(r["video"])}" target="_blank" rel="noopener"' if has_video else ""
    cls = "class-card" if has_video else "class-card class-card--soon"
    eyebrow = f'<span class="cc-num">Clase {clase_disp}</span>' if clase_disp else '<span class="cc-num">Workflow</span>'
    status = ('<span class="cc-play">Ver clase '
              '<svg width="11" height="11" viewBox="0 0 11 11" fill="none">'
              '<path d="M2 1l7 4.5L2 10V1z" fill="currentColor"/></svg></span>') if has_video \
        else '<span class="cc-soon">Próximamente</span>'
    search_blob = esc(f'{r["titulo"]} {r["desc"]} {r["modulo"]}'.lower())
    return f'''<{tag} class="{cls}" style="--nivel-accent:{meta['accent']}" data-nivel="{r['nivel']}" data-search="{search_blob}"{href_attr}>
        <div class="cc-top">{eyebrow}<span class="badge {meta['badge']}"><span class="badge-dot"></span>{meta['emoji']} {meta['label']}</span></div>
        <h4 class="cc-title">{esc(r["titulo"])}</h4>
        <p class="cc-desc">{esc(r["desc"]) if r["desc"] else 'Descripción disponible próximamente.'}</p>
        <div class="cc-foot">{status}</div>
    </{tag}>'''


def module_tag_and_name(modulo):
    """'M1 · Bienvenida y Configuración' -> ('M1', 'Bienvenida y Configuración')
       'M_ Campañas Email' -> ('M_', 'Campañas Email')
       'Otros' -> ('＋', 'Otros')"""
    if "·" in modulo:
        num, name = modulo.split("·", 1)
        return num.strip(), name.strip()
    if modulo.startswith("M_"):
        return "M_", modulo[2:].strip()
    m = re.match(r"^(M\d+)\s+(.*)$", modulo)
    if m:
        return m.group(1), m.group(2)
    return "＋", modulo


def module_anchor(categoria, modulo):
    return f"modulo-{slugify(categoria)}-{slugify(modulo)}"


def module_group_html(modulo, rows_subset, tag_class="", anchor_id=None):
    mod_num, mod_name = module_tag_and_name(modulo)
    cards = "\n".join(card_html(r) for r in rows_subset)
    n = len(rows_subset)
    id_attr = f' id="{anchor_id}"' if anchor_id else ""
    return f'''<div class="module-group"{id_attr}>
        <div class="module-head">
            <span class="module-tag {tag_class}">{esc(mod_num)}</span>
            <h3 class="module-name">{esc(mod_name)}</h3>
            <span class="module-count">{n} clase{'s' if n != 1 else ''}</span>
        </div>
        <div class="card-grid">
        {cards}
        </div>
    </div>'''


def nivel_block_html(nivel, rows_subset, categoria):
    meta = NIVEL_META[nivel]
    modules = group_by_modulo(rows_subset)
    groups_html = "\n".join(
        module_group_html(m, rs, anchor_id=module_anchor(categoria, m))
        for m, rs in modules.items()
    )
    return f'''<div class="nivel-block" id="nivel-{nivel}">
        <div class="nivel-head">
            <span class="nivel-chip" style="--nivel-accent:{meta['accent']}">{meta['emoji']} Nivel {meta['label']}</span>
            <span class="nivel-line"></span>
            <span class="nivel-total">{len(rows_subset)} clases</span>
        </div>
        {groups_html}
    </div>'''


def category_body_html(categoria, rows_subset):
    """Devuelve (html_niveles_pills_o_vacio, html_cuerpo) para una categoría."""
    if categoria in CATEGORIES_WITH_NIVEL_SPLIT:
        niveles_presentes = [n for n in NIVEL_ORDER if any(r["nivel"] == n for r in rows_subset)]
        pills = "\n".join(
            f'<a href="#nivel-{n}" class="level-pill" style="--nivel-accent:{NIVEL_META[n]["accent"]}">'
            f'{NIVEL_META[n]["emoji"]} {NIVEL_META[n]["label"]} '
            f'<span>{sum(1 for r in rows_subset if r["nivel"] == n)}</span></a>'
            for n in niveles_presentes
        )
        body = "\n".join(
            nivel_block_html(n, [r for r in rows_subset if r["nivel"] == n], categoria)
            for n in niveles_presentes
        )
        return pills, body
    else:
        modules = group_by_modulo(rows_subset)
        tag_class = "module-tag--otros"
        body = "\n".join(
            module_group_html(m, rs, tag_class, anchor_id=module_anchor(categoria, m))
            for m, rs in modules.items()
        )
        return "", body


def category_modules_ordered(categoria, rows_subset):
    """Lista de nombres de módulo en el orden en que se renderizan para esta categoría."""
    if categoria in CATEGORIES_WITH_NIVEL_SPLIT:
        niveles_presentes = [n for n in NIVEL_ORDER if any(r["nivel"] == n for r in rows_subset)]
        seen = []
        for n in niveles_presentes:
            for r in rows_subset:
                if r["nivel"] == n and r["modulo"] not in seen:
                    seen.append(r["modulo"])
        return seen
    else:
        seen = []
        for r in rows_subset:
            if r["modulo"] not in seen:
                seen.append(r["modulo"])
        return seen


CATEGORY_COPY = {
    "Básicos": "Todo lo que tu equipo necesita para operar el CRM Llamaleads en el día a día, organizado por nivel de dificultad.",
    "Otros Workflows": "Automatizaciones y flujos específicos que amplían lo que puede hacer tu CRM Llamaleads más allá de lo esencial.",
}


def category_section_html(categoria):
    rows_subset = [r for r in rows if r["categoria"] == categoria]
    anchor = slugify(categoria)
    pills, body = category_body_html(categoria, rows_subset)
    pills_html = f'<div class="level-nav">\n{pills}\n</div>' if pills else ""
    copy = CATEGORY_COPY.get(categoria, "")
    return f'''<section class="cat-section" id="{anchor}">
    <div class="wrap">
      <div class="cat-head">
        <div class="cat-eyebrow"><span class="dot"></span>Categoría</div>
        <h2>{esc(categoria)}</h2>
        <p>{esc(copy)}</p>
      </div>
      {pills_html}
      {body}
    </div>
  </section>'''


sections_html = "\n".join(category_section_html(c) for c in categorias_ordenadas)

def nav_menu_html():
    items = []
    for c in categorias_ordenadas:
        rows_subset = [r for r in rows if r["categoria"] == c]
        cat_anchor = slugify(c)
        modulos = category_modules_ordered(c, rows_subset)
        sub_items = "\n".join(
            f'<li><a href="#{module_anchor(c, m)}">{esc(" · ".join(module_tag_and_name(m)))}</a></li>'
            for m in modulos
        )
        items.append(f'''<li class="nav-cat">
      <div class="nav-cat-row">
        <a href="#{cat_anchor}" class="nav-cat-link">{esc(c)}</a>
        <button class="nav-cat-toggle" type="button" aria-expanded="false" aria-label="Mostrar módulos de {esc(c)}">
          <svg width="12" height="8" viewBox="0 0 12 8" fill="none"><path d="M1 1.5L6 6.5L11 1.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </div>
      <ul class="nav-sub">
        {sub_items}
      </ul>
    </li>''')
    return "\n".join(items)


nav_links_html = nav_menu_html()

total_clases = len(rows)
total_modulos = len({r["modulo"] for r in rows})
total_niveles = len({r["nivel"] for r in rows if r["categoria"] in CATEGORIES_WITH_NIVEL_SPLIT})

print("OK: secciones generadas dinámicamente")
print("Categorías:", categorias_ordenadas)
print("total_clases", total_clases, "total_modulos", total_modulos, "total_niveles", total_niveles)

with open(BUILD_DIR / "_sections.html", "w", encoding="utf-8") as f:
    f.write(sections_html)
with open(BUILD_DIR / "_nav.html", "w", encoding="utf-8") as f:
    f.write(nav_links_html)
with open(BUILD_DIR / "_stats.txt", "w", encoding="utf-8") as f:
    f.write(f"{total_clases}|{total_modulos}|{total_niveles}")

# ---------------------------------------------------------------
# 5. JSON de cursos para el buscador y el asistente
# ---------------------------------------------------------------

courses_for_json = []
for r in rows:
    anchor = f'#nivel-{r["nivel"]}' if r["categoria"] in CATEGORIES_WITH_NIVEL_SPLIT else f'#{slugify(r["categoria"])}'
    courses_for_json.append({
        "clase": clase_display(r["clase"]),
        "titulo": r["titulo"],
        "desc": r["desc"],
        "modulo": r["modulo"],
        "nivel": NIVEL_META[r["nivel"]]["label"],
        "video": r["video"],
        "categoria": r["categoria"],
        "anchor": anchor,
    })

with open(BUILD_DIR / "_courses.json", "w", encoding="utf-8") as f:
    json.dump(courses_for_json, f, ensure_ascii=False)

print("courses.json:", len(courses_for_json), "cursos")
