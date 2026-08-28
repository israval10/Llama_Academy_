# Llama_Academy

Sitio de capacitación **LlamaLeads Academy** — catálogo de cursos para
aprender a usar el **CRM Llamaleads**, con:

- Buscador en vivo (filtra por título, descripción y módulo)
- Asistente tipo chatbot (sugiere clases según palabras clave)
- Tema oscuro con halo "flame" animado en el hero
- Navbar flotante en vidrio esmerilado con menú hamburguesa (en todas las
  resoluciones) — cada categoría se despliega en un acordeón con acceso
  directo a cada uno de sus módulos
- Barra de búsqueda + asistente flotante (sticky) que acompaña al usuario
  al recorrer el catálogo
- Carrusel de clases por módulo (flechas + indicador de progreso), en
  desktop y mobile

Es un único archivo `index.html` autocontenido (sin backend, sin build
step para el usuario final), generado a partir de los datos de la base de
Notion `//Llama_Academy`.

🔗 Abrir `index.html` directamente en el navegador, o subirlo a cualquier
hosting estático (Netlify, GitHub Pages, etc.).

## Estructura del repo

```
Llama_Academy/
├── index.html          ← el sitio final (deliverable, se regenera con los scripts)
├── data/
│   └── rows.json        ← volcado de la base de Notion (fuente de verdad)
├── assets/
│   ├── logo-mark.png     ← mascota / ícono de marca
│   └── logo-wordmark.png ← logo con texto
├── scripts/
│   ├── build.py          ← agrupa los datos: Categoría → (Nivel →) Módulo
│   └── shell.py           ← arma el index.html final (HTML + CSS + JS embebidos)
└── build/                ← archivos intermedios (se regeneran, no se versionan)
```

## Cómo funciona la generación

`build.py` **no tiene ningún nombre de módulo o categoría hardcodeado**.
Agrupa dinámicamente lo que exista en `data/rows.json`:

- **Básicos** (o cualquier categoría en `CATEGORIES_WITH_NIVEL_SPLIT`)
  → se organiza por **Nivel**, y dentro de cada nivel por **Módulo**.
- **Otros Workflows** (o cualquier categoría nueva que aparezca) → se
  organiza directo por **Módulo**, en el orden en que aparecen los datos.

Esto significa que si agregás una subcategoría o módulo nuevo en Notion,
**no hay que tocar el código** — solo actualizar `data/rows.json` y
regenerar.

## Actualizar el sitio cuando cambian los datos en Notion

1. Volver a exportar/consultar la base de Notion `//Llama_Academy`
   (columnas: `Clase`, `Título`, `Descripción`, `Módulo`, `Nivel`,
   `CATEGORY`, `VIDEO`) y sobreescribir `data/rows.json` con el resultado.
2. Regenerar el sitio:

   ```bash
   cd scripts
   python3 build.py   # agrupa los datos y arma las secciones intermedias en build/
   python3 shell.py   # arma el index.html final en la raíz del repo
   ```

3. Commitear y pushear `index.html` (y `data/rows.json` si cambió).

## Campos esperados en `data/rows.json`

Cada fila es un objeto con estas claves (igual a las columnas de Notion):

| Campo | Ejemplo | Notas |
|---|---|---|
| `Clase` | `"601"` | Código de clase (módulo+número). `null` para workflows sin numerar. |
| `Título` | `"¿Qué es un pipeline de ventas?"` | |
| `Descripción` | `"..."` | Puede ser `null`. |
| `Módulo` | `"M4 · Pipelines y Oportunidades"` | El texto que aparece como encabezado de grupo. |
| `Nivel` | `"🟢 Inicial"` / `"🔵 Intermedio"` / `"🟣 Avanzado"` | Se detecta por palabra clave, tolera cambios de emoji. |
| `CATEGORY` | `"Básicos"` / `"Otros Workflows"` | Cualquier valor nuevo se agrega solo como sección nueva. |
| `VIDEO` | URL de Google Drive | Si falta, la clase se muestra como "Próximamente" (no clicable). |

## Marca

Construido siguiendo los brand guidelines de LlamaLeads: amarillo `#F1C721`,
rojo `#DB0000`, negro `#020201`, tipografía Sora (títulos) + Inter (cuerpo).
El CRM siempre se menciona como **"CRM Llamaleads"** — nunca GHL.
