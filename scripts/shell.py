#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD_DIR = ROOT / "build"
ASSETS_DIR = ROOT / "assets"
OUTPUT_DIR = ROOT

with open(BUILD_DIR / "_sections.html", encoding="utf-8") as f:
    SECTIONS_HTML = f.read()
with open(BUILD_DIR / "_nav.html", encoding="utf-8") as f:
    NAV_HTML = f.read()
with open(BUILD_DIR / "_stats.txt") as f:
    total_clases, total_modulos, total_niveles = f.read().split("|")
MARK_B64 = base64.b64encode((ASSETS_DIR / "logo-mark.png").read_bytes()).decode()
WORDMARK_B64 = base64.b64encode((ASSETS_DIR / "logo-wordmark.png").read_bytes()).decode()
with open(BUILD_DIR / "_courses.json", encoding="utf-8") as f:
    COURSES_JSON = f.read()

HTML = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LlamaLeads Academy — Aprende el CRM Llamaleads</title>
<meta name="description" content="Capacitación oficial de LlamaLeads: aprende a usar el CRM Llamaleads clase por clase, organizado por nivel y módulo.">
<link rel="icon" href="data:image/png;base64,{MARK_B64}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{
  --yellow:#F1C721;
  --yellow-50:#F3D046;
  --yellow-40:#F6DA6B;
  --yellow-20:#FAECB5;
  --yellow-10:#FCF4D3;
  --red:#DB0000;
  --red-50:#E12A2A;
  --red-20:#F3AAAA;
  --red-10:#F8CCCC;
  --ink:#020201;
  --ink-50:#2C2C2B;
  --ink-40:#565656;
  --ink-30:#818180;
  --ink-20:#ABABAA;
  --ink-10:#CCCCCC;
  --paper:#FAFAFA;
  --paper-50:#FBFBFB;
  --white:#FFFFFF;
  --page-bg:#F0F0EE;

  --font-display:'Sora', sans-serif;
  --font-body:'Inter', sans-serif;

  --radius-sm:8px;
  --radius-md:14px;
  --radius-lg:22px;
  --radius-pill:999px;

  --shadow-sm:0 1px 2px rgba(2,2,1,0.06), 0 1px 1px rgba(2,2,1,0.04);
  --shadow-md:0 8px 24px rgba(2,2,1,0.08), 0 2px 6px rgba(2,2,1,0.05);
  --shadow-lg:0 20px 48px rgba(2,2,1,0.16), 0 4px 12px rgba(2,2,1,0.06);

  --brand-mark: url("data:image/png;base64,{MARK_B64}");
}}
.brand-icon{{
  display:inline-block; background-image:var(--brand-mark);
  background-size:contain; background-repeat:no-repeat; background-position:center;
  flex:none;
}}

*{{box-sizing:border-box;}}
html{{scroll-behavior:smooth;}}
body{{
  margin:0;
  font-family:var(--font-body);
  color:var(--ink);
  background:var(--page-bg);
  line-height:1.55;
}}
::selection{{ background:var(--yellow); color:var(--ink); }}
a{{ color:var(--red); }}
img{{max-width:100%; display:block;}}
.wrap{{ max-width:1220px; margin:0 auto; padding:0 32px; }}
h1,h2,h3,h4{{ font-family:var(--font-display); margin:0; }}

/* ---------- NAV ---------- */
.nav{{
  position:sticky; top:0; z-index:50;
  background:rgba(250,250,250,0.88);
  backdrop-filter:blur(10px);
  border-bottom:1px solid var(--ink-10);
}}
.nav-inner{{
  max-width:1220px; margin:0 auto; padding:12px 32px;
  display:flex; align-items:center; justify-content:space-between; gap:24px;
}}
.nav-brand{{ display:flex; align-items:center; gap:10px; text-decoration:none; color:var(--ink); }}
.nav-brand .brand-icon{{ width:34px; height:34px; }}
.nav-brand span{{ font-family:var(--font-display); font-weight:700; font-size:16px; letter-spacing:-.2px; }}
.nav-brand small{{ display:block; font-family:var(--font-body); font-weight:600; font-size:10px; letter-spacing:.09em; text-transform:uppercase; color:var(--ink-30); }}
.nav-links{{ display:flex; gap:8px; list-style:none; margin:0; padding:0; }}
.nav-links a{{
  color:var(--ink-50); text-decoration:none; font-size:13.5px; font-weight:700;
  padding:9px 16px; border-radius:var(--radius-pill); transition:.15s;
}}
.nav-links a:hover{{ background:var(--ink-10); color:var(--ink); }}
@media (max-width:720px){{ .nav-links{{ display:none; }} }}

/* ---------- HERO ---------- */
.hero{{
  background:var(--ink);
  color:var(--paper);
  padding:76px 0 96px;
  position:relative;
  overflow:hidden;
}}
.hero::before{{
  content:"";
  position:absolute; right:-140px; top:-160px; width:520px; height:520px; z-index:0;
  background:radial-gradient(circle, var(--yellow) 0%, transparent 68%);
  opacity:.30; pointer-events:none;
  animation: heroDrift1 17s ease-in-out infinite;
}}
.hero::after{{
  content:"";
  position:absolute; left:-120px; bottom:-200px; width:420px; height:420px; z-index:0;
  background:radial-gradient(circle, var(--red) 0%, transparent 70%);
  opacity:.22; pointer-events:none;
  animation: heroDrift2 21s ease-in-out infinite;
}}
.hero-glow{{
  position:absolute; z-index:0; width:640px; height:640px; border-radius:50%;
  left:var(--mx, 50%); top:var(--my, 32%); transform:translate(-50%,-50%);
  background:radial-gradient(circle, rgba(241,199,33,0.32) 0%, rgba(219,0,0,0.10) 45%, transparent 72%);
  filter:blur(6px); opacity:0; transition:opacity .5s ease; pointer-events:none;
}}
.hero:hover .hero-glow{{ opacity:1; }}

@keyframes heroDrift1{{
  0%,100%{{ transform:translate(0,0) scale(1); }}
  50%{{ transform:translate(-46px,34px) scale(1.09); }}
}}
@keyframes heroDrift2{{
  0%,100%{{ transform:translate(0,0) scale(1); }}
  50%{{ transform:translate(38px,-42px) scale(1.12); }}
}}
@media (prefers-reduced-motion: reduce){{
  .hero::before, .hero::after{{ animation:none; }}
  .hero-glow{{ transition:none; opacity:0 !important; }}
}}
.hero-inner{{ position:relative; z-index:1; display:flex; flex-direction:column; align-items:center; text-align:center; }}
.hero-copy{{ max-width:720px; display:flex; flex-direction:column; align-items:center; }}
.hero-eyebrow{{
  display:inline-flex; align-items:center; gap:8px;
  font-family:var(--font-body); font-weight:700; font-size:12px; letter-spacing:.09em;
  text-transform:uppercase; color:var(--yellow); margin:0 0 18px; padding:6px 14px 6px 8px;
  border:1px solid rgba(241,199,33,0.35); border-radius:var(--radius-pill);
}}
.hero-eyebrow .brand-icon{{ width:18px; height:18px; }}
.hero-copy h1{{ font-size:clamp(34px,4.6vw,54px); line-height:1.06; margin:0 0 20px; letter-spacing:-1px; }}
.hero-copy h1 em{{ font-style:normal; color:var(--yellow); }}
.hero-copy p{{ color:var(--ink-10); font-size:17.5px; max-width:560px; margin:0 0 32px; opacity:.9; }}
.hero-actions{{ display:flex; gap:14px; flex-wrap:wrap; justify-content:center; }}
.btn{{
  font-family:var(--font-body); font-weight:700; font-size:14.5px;
  border-radius:var(--radius-pill); border:2px solid transparent;
  padding:13px 24px; cursor:pointer; display:inline-flex; align-items:center; gap:8px;
  transition:transform .12s ease, box-shadow .12s ease, background .15s ease;
  text-decoration:none; line-height:1;
}}
.btn-accent{{ background:var(--yellow); color:var(--ink); }}
.btn-accent:hover{{ box-shadow:0 10px 26px rgba(241,199,33,.4); transform:translateY(-1px); }}
.btn-outline{{ background:transparent; border-color:rgba(250,250,250,0.35); color:var(--paper); }}
.btn-outline:hover{{ background:rgba(250,250,250,0.1); border-color:var(--paper); }}

@media (max-width:720px){{
  .hero{{ padding:56px 0 64px; }}
}}

/* ---------- TOOLBAR: BUSCADOR + ASISTENTE ---------- */
.toolbar{{
  background:var(--white); border-bottom:1px solid var(--ink-10);
  padding:26px 0; position:relative; z-index:20;
}}
.toolbar-inner{{ display:flex; gap:14px; align-items:flex-start; flex-wrap:wrap; }}
.search-box{{
  flex:1 1 340px; position:relative; display:flex; align-items:center;
  background:var(--paper-50); border:1.5px solid var(--ink-10); border-radius:var(--radius-pill);
  padding:0 6px 0 18px; transition:border-color .15s, box-shadow .15s;
}}
.search-box:focus-within{{ border-color:var(--yellow); box-shadow:0 0 0 4px rgba(241,199,33,.22); background:var(--white); }}
.search-box svg{{ flex:none; color:var(--ink-30); }}
.search-box input{{
  flex:1; border:none; background:transparent; outline:none;
  font-family:var(--font-body); font-size:14.5px; color:var(--ink); padding:13px 10px;
}}
.search-box input::placeholder{{ color:var(--ink-30); }}
.search-clear{{
  flex:none; display:none; align-items:center; justify-content:center; width:28px; height:28px;
  border:none; border-radius:50%; background:var(--ink-10); color:var(--ink-50); cursor:pointer; font-size:13px;
}}
.search-clear:hover{{ background:var(--ink-20); }}
.search-count{{ font-size:11.5px; color:var(--ink-30); font-weight:600; padding:0 12px 0 2px; white-space:nowrap; }}

.assistant-toggle{{
  flex:0 0 auto; display:inline-flex; align-items:center; gap:10px;
  background:var(--ink); color:var(--paper); border:none; border-radius:var(--radius-pill);
  padding:10px 20px 10px 10px; cursor:pointer; font-family:var(--font-body); font-weight:700; font-size:14px;
  transition:transform .12s ease, box-shadow .12s ease;
}}
.assistant-toggle:hover{{ box-shadow:0 8px 20px rgba(2,2,1,.24); transform:translateY(-1px); }}
.assistant-toggle .brand-icon{{ width:30px; height:30px; border-radius:50%; background:var(--yellow); padding:3px; box-sizing:border-box; }}
.assistant-toggle .at-dot{{ width:7px; height:7px; border-radius:50%; background:#3FCB6B; box-shadow:0 0 0 3px rgba(63,203,107,.25); }}

.no-results{{ display:none; text-align:center; padding:60px 20px; color:var(--ink-40); }}
.no-results .brand-icon{{ width:64px; height:64px; margin:0 auto 14px; opacity:.7; }}
.no-results h3{{ font-size:19px; margin-bottom:6px; color:var(--ink); }}
.no-results p{{ font-size:14px; margin:0; }}
.is-hidden{{ display:none !important; }}

/* Chat panel */
.chat-panel{{
  max-height:0; overflow:hidden; opacity:0;
  transition:max-height .32s ease, opacity .25s ease, margin .3s ease;
  margin-top:0;
}}
.chat-panel.is-open{{ max-height:640px; opacity:1; margin-top:16px; }}
.chat-shell{{
  background:var(--ink); border-radius:var(--radius-lg); overflow:hidden; box-shadow:var(--shadow-lg);
  display:flex; flex-direction:column; max-width:640px;
}}
.chat-head{{ display:flex; align-items:center; gap:10px; padding:16px 18px; border-bottom:1px solid rgba(250,250,250,.1); }}
.chat-head .brand-icon{{ width:32px; height:32px; }}
.chat-head b{{ display:block; font-family:var(--font-display); font-size:14px; color:var(--paper); }}
.chat-head small{{ color:var(--ink-10); opacity:.65; font-size:11.5px; }}
.chat-close{{ margin-left:auto; background:none; border:none; color:var(--ink-10); opacity:.7; cursor:pointer; font-size:18px; line-height:1; padding:4px; }}
.chat-close:hover{{ opacity:1; }}
.chat-body{{ padding:18px; display:flex; flex-direction:column; gap:12px; max-height:340px; overflow-y:auto; background:#141412; }}
.chat-msg{{ display:flex; gap:10px; max-width:88%; }}
.chat-msg.user{{ align-self:flex-end; flex-direction:row-reverse; }}
.chat-msg .bubble{{
  background:var(--paper-50); color:var(--ink); border-radius:14px 14px 14px 4px; padding:10px 14px;
  font-size:13.5px; line-height:1.5;
}}
.chat-msg.user .bubble{{ background:var(--yellow); border-radius:14px 14px 4px 14px; font-weight:600; }}
.chat-msg .avatar{{ width:26px; height:26px; flex:none; border-radius:50%; background:var(--yellow); padding:4px; box-sizing:border-box; }}
.chat-suggest{{ display:flex; flex-direction:column; gap:6px; margin-top:8px; }}
.chat-suggest a{{
  display:flex; align-items:center; justify-content:space-between; gap:8px;
  background:var(--white); border:1px solid var(--ink-10); border-radius:10px; padding:9px 12px;
  text-decoration:none; color:var(--ink); font-size:12.5px; font-weight:700;
}}
.chat-suggest a:hover{{ border-color:var(--red); }}
.chat-suggest a span.tag{{ font-weight:600; color:var(--ink-30); font-size:11px; }}
.chat-chips{{ display:flex; gap:8px; flex-wrap:wrap; padding:0 18px 14px; }}
.chat-chip{{
  background:rgba(250,250,250,.08); border:1px solid rgba(250,250,250,.16); color:var(--ink-10);
  font-size:12px; font-weight:600; padding:7px 13px; border-radius:var(--radius-pill); cursor:pointer;
}}
.chat-chip:hover{{ background:rgba(241,199,33,.16); border-color:var(--yellow); color:var(--yellow); }}
.chat-input-row{{ display:flex; gap:8px; padding:14px 18px; border-top:1px solid rgba(250,250,250,.1); }}
.chat-input-row input{{
  flex:1; background:rgba(250,250,250,.07); border:1px solid rgba(250,250,250,.15); border-radius:var(--radius-pill);
  padding:11px 16px; color:var(--paper); font-family:var(--font-body); font-size:13.5px; outline:none;
}}
.chat-input-row input::placeholder{{ color:var(--ink-20); }}
.chat-input-row input:focus{{ border-color:var(--yellow); }}
.chat-send{{
  background:var(--yellow); color:var(--ink); border:none; border-radius:50%; width:38px; height:38px;
  flex:none; cursor:pointer; display:flex; align-items:center; justify-content:center;
}}
.chat-send:hover{{ background:var(--yellow-50); }}

@media (max-width:640px){{
  .toolbar-inner{{ flex-direction:column; }}
  .search-box{{ flex:none; width:100%; }}
  .assistant-toggle{{ width:100%; justify-content:center; }}
  .chat-shell{{ max-width:100%; }}
}}

/* ---------- CATEGORY SECTIONS ---------- */
.cat-section{{ padding:72px 0; border-bottom:1px solid var(--ink-10); }}
.cat-section:last-of-type{{ border-bottom:none; }}
.cat-head{{ max-width:680px; margin-bottom:34px; }}
.cat-eyebrow{{
  font-family:var(--font-body); font-weight:700; font-size:12px; letter-spacing:.08em;
  text-transform:uppercase; color:var(--red); margin:0 0 10px; display:flex; align-items:center; gap:8px;
}}
.cat-eyebrow .dot{{ width:7px; height:7px; border-radius:50%; background:var(--red); }}
.cat-head h2{{ font-size:clamp(28px,3.4vw,38px); margin:0 0 12px; letter-spacing:-.6px; }}
.cat-head p{{ color:var(--ink-40); font-size:15.5px; margin:0; }}

.level-nav{{ display:flex; gap:10px; flex-wrap:wrap; margin-bottom:44px; }}
.level-pill{{
  --nivel-accent: var(--yellow);
  display:inline-flex; align-items:center; gap:8px;
  background:var(--white); border:1.5px solid var(--ink-10); text-decoration:none; color:var(--ink);
  font-family:var(--font-body); font-weight:700; font-size:13.5px;
  padding:10px 18px; border-radius:var(--radius-pill); transition:.15s;
}}
.level-pill:hover{{ border-color:var(--nivel-accent); box-shadow:0 4px 14px rgba(2,2,1,0.08); transform:translateY(-1px); }}
.level-pill span{{ background:var(--nivel-accent); color:var(--white); font-size:11.5px; padding:2px 8px; border-radius:var(--radius-pill); }}

.nivel-block{{ margin-bottom:8px; }}
.nivel-head{{ display:flex; align-items:center; gap:14px; margin:0 0 26px; }}
.nivel-chip{{
  --nivel-accent: var(--yellow);
  font-family:var(--font-display); font-weight:700; font-size:17px;
  color:var(--ink); display:flex; align-items:center; gap:8px;
  padding-bottom:4px; border-bottom:3px solid var(--nivel-accent);
}}
.nivel-line{{ flex:1; height:1px; background:var(--ink-10); }}
.nivel-total{{ font-size:12.5px; color:var(--ink-30); font-weight:600; white-space:nowrap; }}

.module-group{{ margin-bottom:40px; }}
.module-head{{ display:flex; align-items:baseline; gap:12px; margin-bottom:16px; flex-wrap:wrap; }}
.module-tag{{
  font-family:var(--font-display); font-weight:800; font-size:12px;
  background:var(--ink); color:var(--yellow); padding:4px 10px; border-radius:7px; letter-spacing:.02em;
}}
.module-tag--otros{{ background:var(--red); color:var(--white); }}
.module-name{{ font-size:18px; font-weight:700; letter-spacing:-.2px; }}
.module-count{{ font-size:12px; color:var(--ink-30); font-weight:600; margin-left:auto; }}

/* ---------- CARDS ---------- */
.card-grid{{ display:grid; grid-template-columns:repeat(auto-fill,minmax(272px,1fr)); gap:16px; }}
.class-card{{
  --nivel-accent: var(--yellow);
  display:block; text-decoration:none; color:var(--ink);
  background:var(--white); border:1px solid var(--ink-10); border-top:4px solid var(--nivel-accent);
  border-radius:var(--radius-md); padding:20px 20px 18px;
  box-shadow:var(--shadow-sm);
  transition:box-shadow .18s ease, transform .18s ease, border-color .18s ease;
  position:relative;
}}
.class-card:hover{{ box-shadow:var(--shadow-md); transform:translateY(-3px); }}
.class-card--soon{{ cursor:default; opacity:.72; }}
.class-card--soon:hover{{ transform:none; box-shadow:var(--shadow-sm); }}
.cc-top{{ display:flex; align-items:center; justify-content:space-between; gap:8px; margin-bottom:12px; }}
.cc-num{{ font-family:var(--font-display); font-weight:700; font-size:11.5px; color:var(--ink-30); letter-spacing:.03em; }}
.badge{{
  display:inline-flex; align-items:center; gap:5px;
  font-size:10.5px; font-weight:700; padding:4px 10px; border-radius:var(--radius-pill);
  font-family:var(--font-body); white-space:nowrap;
}}
.badge-dot{{ width:5px; height:5px; border-radius:50%; }}
.badge-yellow{{ background:var(--yellow-10); color:#7A5E00; }}
.badge-yellow .badge-dot{{ background:var(--yellow); }}
.badge-red{{ background:var(--red-10); color:#8A0000; }}
.badge-red .badge-dot{{ background:var(--red); }}
.badge-ink{{ background:var(--ink-10); color:var(--ink-50); }}
.badge-ink .badge-dot{{ background:var(--ink-50); }}
.cc-title{{ font-family:var(--font-display); font-size:15.5px; font-weight:700; line-height:1.32; margin:0 0 8px; letter-spacing:-.1px; }}
.cc-desc{{ font-size:13px; color:var(--ink-40); margin:0 0 16px; line-height:1.5; }}
.cc-foot{{ display:flex; align-items:center; }}
.cc-play{{ display:inline-flex; align-items:center; gap:6px; font-size:12.5px; font-weight:700; color:var(--red); }}
.class-card:hover .cc-play{{ text-decoration:underline; }}
.cc-soon{{ font-size:12px; font-weight:700; color:var(--ink-30); text-transform:uppercase; letter-spacing:.04em; }}

/* ---------- FOOTER ---------- */
.site-footer{{ background:var(--ink); color:var(--ink-10); padding:44px 0; }}
.footer-inner{{ display:flex; align-items:center; justify-content:space-between; gap:20px; flex-wrap:wrap; }}
.footer-brand{{ display:flex; align-items:center; gap:10px; }}
.footer-brand .brand-icon{{ width:24px; height:24px; }}
.footer-brand span{{ font-family:var(--font-display); font-weight:700; font-size:14px; color:var(--paper); }}
.site-footer p{{ margin:0; font-size:12.5px; opacity:.65; }}

@media (max-width:640px){{
  .wrap{{ padding:0 20px; }}
  .card-grid{{ grid-template-columns:1fr; }}
}}
</style>
</head>
<body>

<nav class="nav">
  <div class="nav-inner">
    <a class="nav-brand" href="#top">
      <span class="brand-icon" role="img" aria-label="Llamaleads"></span>
      <div><span>LlamaLeads Academy</span><small>Capacitación CRM Llamaleads</small></div>
    </a>
    <ul class="nav-links">
      {NAV_HTML}
    </ul>
  </div>
</nav>

<header class="hero" id="top">
  <div class="hero-glow" id="heroGlow"></div>
  <div class="wrap hero-inner">
    <div class="hero-copy">
      <div class="hero-eyebrow"><span class="brand-icon" role="img" aria-label=""></span> Academia oficial de Llamaleads</div>
      <h1>Aprende el CRM <em>Llamaleads</em><br>clase por clase.</h1>
      <p>Cursos cortos y directos al grano para que tu equipo domine el CRM Llamaleads desde el primer día: configuración, contactos, pipelines, conversaciones y mucho más.</p>
      <div class="hero-actions">
        <a href="#basicos" class="btn btn-accent">Empezar por Básicos →</a>
        <a href="#otros-workflows" class="btn btn-outline">Ver otros workflows</a>
      </div>
    </div>
  </div>
</header>

<section class="toolbar" id="toolbar">
  <div class="wrap">
    <div class="toolbar-inner">
      <div class="search-box">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="7" cy="7" r="5.5" stroke="currentColor" stroke-width="1.6"/><path d="M11.5 11.5L15 15" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
        <input type="text" id="searchInput" placeholder="Buscar una clase: pipelines, WhatsApp, contactos, tags…" autocomplete="off">
        <span class="search-count" id="searchCount"></span>
        <button class="search-clear" id="searchClear" type="button" aria-label="Limpiar búsqueda">✕</button>
      </div>
      <button class="assistant-toggle" id="assistantToggle" type="button">
        <span class="brand-icon" role="img" aria-label=""></span>
        Pregúntale a la llama
        <span class="at-dot"></span>
      </button>
    </div>

    <div class="chat-panel" id="chatPanel">
      <div class="chat-shell">
        <div class="chat-head">
          <span class="brand-icon" role="img" aria-label=""></span>
          <div><b>Asistente Llamaleads</b><small>Te ayudo a encontrar la clase correcta</small></div>
          <button class="chat-close" id="chatClose" type="button" aria-label="Cerrar asistente">✕</button>
        </div>
        <div class="chat-body" id="chatBody">
          <div class="chat-msg bot">
            <span class="brand-icon avatar" role="img" aria-label=""></span>
            <div class="bubble">¡Hola! 🦙 Soy el asistente de LlamaLeads Academy. Contame qué querés hacer en el CRM Llamaleads y te recomiendo la clase justa.</div>
          </div>
        </div>
        <div class="chat-chips">
          <button class="chat-chip" type="button" data-q="¿Cómo conecto WhatsApp?">¿Cómo conecto WhatsApp?</button>
          <button class="chat-chip" type="button" data-q="¿Qué es un pipeline?">¿Qué es un pipeline?</button>
          <button class="chat-chip" type="button" data-q="Importar contactos desde CSV">Importar contactos CSV</button>
          <button class="chat-chip" type="button" data-q="Campos personalizados">Campos personalizados</button>
        </div>
        <form class="chat-input-row" id="chatForm">
          <input type="text" id="chatInput" placeholder="Escribí tu pregunta sobre el CRM Llamaleads…" autocomplete="off">
          <button class="chat-send" type="submit" aria-label="Enviar">
            <svg width="15" height="15" viewBox="0 0 15 15" fill="none"><path d="M1 7.5L13.5 1.5L9.5 13.5L7 8L1 7.5Z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/></svg>
          </button>
        </form>
      </div>
    </div>
  </div>
</section>

<main>
  <div class="wrap">
    <div class="no-results" id="noResults">
      <span class="brand-icon" role="img" aria-label=""></span>
      <h3>No encontramos clases con esa búsqueda</h3>
      <p>Probá con otra palabra clave o preguntale al asistente 🦙</p>
    </div>
  </div>

  {SECTIONS_HTML}
</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div class="footer-brand">
      <span class="brand-icon" role="img" aria-label="Llamaleads"></span>
      <span>LlamaLeads Academy</span>
    </div>
    <p>© LlamaLeads · Capacitación interna del CRM Llamaleads para clientes y equipo.</p>
  </div>
</footer>

<script>
const COURSES = {COURSES_JSON};

/* ---------------- Glow interactivo del hero ---------------- */
(function() {{
  const hero = document.querySelector('.hero');
  const glow = document.getElementById('heroGlow');
  if (!hero || !glow) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  let targetX = 50, targetY = 32, curX = 50, curY = 32;

  hero.addEventListener('mousemove', (e) => {{
    const rect = hero.getBoundingClientRect();
    targetX = ((e.clientX - rect.left) / rect.width) * 100;
    targetY = ((e.clientY - rect.top) / rect.height) * 100;
  }});

  function tick() {{
    curX += (targetX - curX) * 0.07;
    curY += (targetY - curY) * 0.07;
    glow.style.setProperty('--mx', curX.toFixed(2) + '%');
    glow.style.setProperty('--my', curY.toFixed(2) + '%');
    requestAnimationFrame(tick);
  }}
  tick();
}})();

/* ---------------- Buscador ---------------- */
(function() {{
  const input = document.getElementById('searchInput');
  const clearBtn = document.getElementById('searchClear');
  const countEl = document.getElementById('searchCount');
  const noResults = document.getElementById('noResults');
  const cards = Array.from(document.querySelectorAll('.class-card'));
  const moduleGroups = Array.from(document.querySelectorAll('.module-group'));
  const nivelBlocks = Array.from(document.querySelectorAll('.nivel-block'));
  const catSections = Array.from(document.querySelectorAll('.cat-section'));

  function runSearch() {{
    const q = input.value.trim().toLowerCase();
    clearBtn.style.display = q ? 'flex' : 'none';

    if (!q) {{
      cards.forEach(c => c.classList.remove('is-hidden'));
      moduleGroups.forEach(g => g.classList.remove('is-hidden'));
      nivelBlocks.forEach(b => b.classList.remove('is-hidden'));
      catSections.forEach(s => s.classList.remove('is-hidden'));
      noResults.style.display = 'none';
      countEl.textContent = '';
      return;
    }}

    let visibleTotal = 0;
    const terms = q.split(/\\s+/).filter(Boolean);

    moduleGroups.forEach(group => {{
      let groupHasMatch = false;
      group.querySelectorAll('.class-card').forEach(card => {{
        const blob = card.getAttribute('data-search') || '';
        const match = terms.every(t => blob.includes(t));
        card.classList.toggle('is-hidden', !match);
        if (match) {{ groupHasMatch = true; visibleTotal++; }}
      }});
      group.classList.toggle('is-hidden', !groupHasMatch);
    }});

    nivelBlocks.forEach(block => {{
      const hasVisible = block.querySelector('.module-group:not(.is-hidden)');
      block.classList.toggle('is-hidden', !hasVisible);
    }});

    catSections.forEach(sec => {{
      const hasVisible = sec.querySelector('.class-card:not(.is-hidden)');
      sec.classList.toggle('is-hidden', !hasVisible);
    }});

    noResults.style.display = visibleTotal === 0 ? 'block' : 'none';
    countEl.textContent = visibleTotal + (visibleTotal === 1 ? ' resultado' : ' resultados');
  }}

  input.addEventListener('input', runSearch);
  clearBtn.addEventListener('click', () => {{
    input.value = '';
    runSearch();
    input.focus();
  }});
}})();

/* ---------------- Asistente ---------------- */
(function() {{
  const toggle = document.getElementById('assistantToggle');
  const closeBtn = document.getElementById('chatClose');
  const panel = document.getElementById('chatPanel');
  const body = document.getElementById('chatBody');
  const form = document.getElementById('chatForm');
  const chatInput = document.getElementById('chatInput');
  const chips = document.querySelectorAll('.chat-chip');

  const STOPWORDS = new Set(['que','como','cómo','qué','para','del','las','los','una','uno','con','por','se','el','la','en','de','y','a','al','es','tu','mi','como','puedo','quiero','necesito','sobre','me']);

  function tokenize(str) {{
    return str.toLowerCase()
      .normalize('NFD').replace(/[\\u0300-\\u036f]/g, '')
      .replace(/[^a-z0-9\\s]/g, ' ')
      .split(/\\s+/)
      .filter(t => t.length > 2 && !STOPWORDS.has(t));
  }}

  function scoreCourse(course, tokens) {{
    const blob = (course.titulo + ' ' + course.desc + ' ' + course.modulo)
      .toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g, '');
    let score = 0;
    tokens.forEach(t => {{ if (blob.includes(t)) score += 1; }});
    return score;
  }}

  function addMessage(html, isUser) {{
    const wrap = document.createElement('div');
    wrap.className = 'chat-msg ' + (isUser ? 'user' : 'bot');
    if (!isUser) {{
      wrap.innerHTML = '<span class="brand-icon avatar" role="img" aria-label=""></span><div class="bubble">' + html + '</div>';
    }} else {{
      wrap.innerHTML = '<div class="bubble"></div>';
      wrap.querySelector('.bubble').textContent = html;
    }}
    body.appendChild(wrap);
    body.scrollTop = body.scrollHeight;
  }}

  function respond(query) {{
    const tokens = tokenize(query);
    if (!tokens.length) {{
      addMessage('¿Podés darme un poco más de detalle? Por ejemplo: "cómo importo contactos" o "qué es un pipeline".', false);
      return;
    }}
    const scored = COURSES
      .map(c => ({{ c, score: scoreCourse(c, tokens) }}))
      .filter(x => x.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, 3);

    if (!scored.length) {{
      addMessage('No encontré una clase exacta para eso todavía. Probá con otras palabras o mirá la sección de <b>Básicos</b> — seguro está por ahí 🦙', false);
      return;
    }}

    let html = scored.length === 1
      ? 'Esta es la clase que buscás:'
      : 'Estas clases te van a servir:';
    html += '<div class="chat-suggest">';
    scored.forEach(({{ c }}) => {{
      const numLabel = c.clase ? ('Clase ' + c.clase) : 'Workflow';
      if (c.video) {{
        html += '<a href="' + c.video + '" target="_blank" rel="noopener">' + c.titulo + '<span class="tag">' + numLabel + '</span></a>';
      }} else {{
        html += '<a href="' + c.anchor + '" style="opacity:.7">' + c.titulo + '<span class="tag">Próximamente</span></a>';
      }}
    }});
    html += '</div>';
    addMessage(html, false);
  }}

  function openPanel() {{
    panel.classList.add('is-open');
    setTimeout(() => chatInput.focus(), 250);
  }}
  function closePanel() {{ panel.classList.remove('is-open'); }}

  toggle.addEventListener('click', () => {{
    panel.classList.contains('is-open') ? closePanel() : openPanel();
  }});
  closeBtn.addEventListener('click', closePanel);

  form.addEventListener('submit', (e) => {{
    e.preventDefault();
    const q = chatInput.value.trim();
    if (!q) return;
    addMessage(q, true);
    chatInput.value = '';
    setTimeout(() => respond(q), 260);
  }});

  chips.forEach(chip => {{
    chip.addEventListener('click', () => {{
      const q = chip.getAttribute('data-q');
      openPanel();
      addMessage(q, true);
      setTimeout(() => respond(q), 260);
    }});
  }});
}})();
</script>

</body>
</html>
'''

with open(OUTPUT_DIR / "index.html", "w", encoding="utf-8") as f:
    f.write(HTML)

print("Escrito:", len(HTML), "caracteres")
