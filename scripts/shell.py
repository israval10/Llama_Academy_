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
  --violet:#A78BFA;
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

  --bg:#0A0A09;
  --bg-alt:#111110;
  --surface:rgba(255,255,255,.035);
  --surface-strong:rgba(255,255,255,.06);
  --line:rgba(255,255,255,.09);
  --line-amber:rgba(241,199,33,.22);
  --text:#F3F2EE;
  --text-dim:rgba(243,242,238,.62);
  --text-faint:rgba(243,242,238,.38);

  --font-display:'Sora', sans-serif;
  --font-body:'Inter', sans-serif;

  --radius-sm:8px;
  --radius-md:14px;
  --radius-lg:22px;
  --radius-pill:999px;

  --shadow-sm:0 1px 3px rgba(0,0,0,0.35);
  --shadow-md:0 14px 34px rgba(0,0,0,0.5);
  --shadow-lg:0 24px 60px rgba(0,0,0,0.6);

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
  color:var(--text);
  background:var(--bg);
  line-height:1.55;
}}
::selection{{ background:var(--yellow); color:var(--ink); }}
a{{ color:var(--yellow); }}
img{{max-width:100%; display:block;}}
.wrap{{ max-width:1220px; margin:0 auto; padding:0 32px; }}
h1,h2,h3,h4{{ font-family:var(--font-display); margin:0; color:var(--text); }}

/* ---------- NAV ---------- */
.nav{{
  position:fixed; top:16px; left:16px; right:16px; z-index:100;
  max-width:1220px; margin:0 auto;
  border:1px solid var(--line-amber); border-radius:22px;
  background:
    radial-gradient(circle at 46% 0%, rgba(241,199,33,.14), transparent 40%),
    radial-gradient(circle at 64% 8%, rgba(219,0,0,.10), transparent 42%),
    rgba(20,19,17,.66);
  box-shadow:0 18px 50px rgba(0,0,0,.5), 0 0 0 1px rgba(255,255,255,.03) inset;
  backdrop-filter:blur(18px) saturate(1.15);
  -webkit-backdrop-filter:blur(18px) saturate(1.15);
}}
.nav-inner{{
  padding:10px 20px;
  display:flex; align-items:center; justify-content:space-between; gap:24px;
}}
.nav-brand{{ display:flex; align-items:center; gap:10px; text-decoration:none; color:var(--text); }}
.nav-brand .brand-icon{{ width:32px; height:32px; }}
.nav-brand span{{ font-family:var(--font-display); font-weight:700; font-size:15px; letter-spacing:-.2px; color:var(--text); }}
.nav-brand small{{ display:block; font-family:var(--font-body); font-weight:600; font-size:9.5px; letter-spacing:.09em; text-transform:uppercase; color:var(--text-faint); }}

.nav-toggle{{
  flex:none; display:inline-flex; flex-direction:column; align-items:center; justify-content:center; gap:5px;
  width:42px; height:42px; border:1px solid rgba(241,199,33,.22); border-radius:13px;
  background:rgba(0,0,0,.22); cursor:pointer; padding:0;
}}
.nav-toggle span{{ width:18px; height:2px; border-radius:999px; background:var(--yellow); transition:transform .22s ease, opacity .22s ease; }}
.nav.is-open .nav-toggle span:nth-child(1){{ transform:translateY(7px) rotate(45deg); }}
.nav.is-open .nav-toggle span:nth-child(2){{ opacity:0; }}
.nav.is-open .nav-toggle span:nth-child(3){{ transform:translateY(-7px) rotate(-45deg); }}
.nav-toggle:hover{{ border-color:rgba(241,199,33,.42); background:rgba(241,199,33,.08); }}

.nav-menu{{
  position:absolute; top:calc(100% + 10px); left:0; right:0;
  list-style:none; margin:0; display:flex; flex-direction:column; gap:6px; padding:12px;
  border:1px solid var(--line-amber); border-radius:18px;
  background:
    radial-gradient(circle at 34% 0%, rgba(241,199,33,.14), transparent 40%),
    rgba(17,16,14,.94);
  box-shadow:0 20px 54px rgba(0,0,0,.55);
  backdrop-filter:blur(18px) saturate(1.1);
  -webkit-backdrop-filter:blur(18px) saturate(1.1);
  opacity:0; visibility:hidden; transform:translateY(-8px); pointer-events:none;
  transition:opacity .22s ease, transform .22s ease, visibility 0s linear .22s;
}}
.nav.is-open .nav-menu{{ opacity:1; visibility:visible; transform:translateY(0); pointer-events:auto; transition:opacity .22s ease, transform .22s ease; }}
.nav-menu{{ max-height:min(70vh, 560px); overflow-y:auto; }}

.nav-cat + .nav-cat{{ margin-top:2px; }}
.nav-cat-row{{
  display:flex; align-items:stretch; gap:6px;
  border:1px solid rgba(241,199,33,.12); border-radius:12px; background:rgba(0,0,0,.18);
  overflow:hidden;
}}
.nav-cat-link{{
  flex:1; display:flex; align-items:center; color:rgba(255,255,255,.86); text-decoration:none;
  font-size:14px; font-weight:800; letter-spacing:.01em; padding:13px 16px;
  transition:color .2s ease, background .2s ease;
}}
.nav-cat-link:hover{{ color:var(--yellow); background:rgba(241,199,33,.08); }}
.nav-cat-toggle{{
  flex:none; width:44px; display:flex; align-items:center; justify-content:center;
  background:transparent; border:none; border-left:1px solid rgba(241,199,33,.12);
  color:rgba(255,255,255,.6); cursor:pointer;
}}
.nav-cat-toggle svg{{ transition:transform .22s ease; }}
.nav-cat-toggle:hover{{ color:var(--yellow); background:rgba(241,199,33,.08); }}
.nav-cat.is-open .nav-cat-toggle svg{{ transform:rotate(180deg); }}

.nav-sub{{
  list-style:none; margin:0; padding:0 0 0 12px;
  max-height:0; overflow:hidden;
  transition:max-height .28s ease;
}}
.nav-cat.is-open .nav-sub{{ max-height:600px; }}
.nav-sub li{{ padding:6px 0 0; }}
.nav-sub li:first-child{{ padding-top:8px; }}
.nav-sub a{{
  display:block; color:rgba(255,255,255,.62); text-decoration:none; font-size:12.5px; font-weight:700;
  padding:10px 14px; border-radius:10px; border:1px solid rgba(255,255,255,.06); background:rgba(255,255,255,.02);
  border-left:2px solid rgba(241,199,33,.3);
  transition:color .2s ease, background .2s ease, border-color .2s ease;
}}
.nav-sub a:hover{{ color:var(--yellow); background:rgba(241,199,33,.08); border-left-color:var(--yellow); }}
@media (max-width:720px){{ .nav{{ left:10px; right:10px; top:10px; }} }}

/* ---------- HERO ---------- */
.hero{{
  background:var(--bg);
  color:var(--text);
  padding:clamp(130px,15vw,164px) 0 100px;
  position:relative;
  overflow:hidden;
}}
/* ── flame orb: halo ambiental que respira solo ── */
.flame-orb{{
  position:absolute; z-index:0; pointer-events:none;
  width:560px; height:560px; top:38%; left:50%;
  margin-left:-280px; margin-top:-280px;
  border-radius:50%; opacity:.55;
  background:radial-gradient(circle at 45% 40%, var(--yellow) 0%, var(--red) 45%, #3D0000 75%, transparent 100%);
  filter:blur(80px);
  animation: flameBreath 4.2s ease-in-out infinite;
}}
@keyframes flameBreath{{
  0%,100%{{ transform:scale(1); }}
  50%{{ transform:scale(1.12); }}
}}
.hero-glow{{
  position:absolute; z-index:0; width:640px; height:640px; border-radius:50%;
  left:var(--mx, 50%); top:var(--my, 32%); transform:translate(-50%,-50%);
  background:radial-gradient(circle, rgba(241,199,33,0.28) 0%, rgba(219,0,0,0.10) 45%, transparent 72%);
  filter:blur(6px); opacity:0; transition:opacity .5s ease; pointer-events:none;
}}
.hero:hover .hero-glow{{ opacity:1; }}
@media (prefers-reduced-motion: reduce){{
  .flame-orb{{ animation:none; }}
  .hero-glow{{ transition:none; opacity:0 !important; }}
}}
.hero-inner{{ position:relative; z-index:1; display:flex; flex-direction:column; align-items:center; text-align:center; }}
.hero-copy{{ max-width:720px; display:flex; flex-direction:column; align-items:center; }}
.hero-eyebrow{{
  display:inline-flex; align-items:center; gap:8px;
  font-family:var(--font-body); font-weight:700; font-size:12px; letter-spacing:.09em;
  text-transform:uppercase; color:var(--yellow); margin:0 0 18px; padding:6px 14px 6px 8px;
  border:1px solid rgba(241,199,33,0.35); border-radius:var(--radius-pill);
  background:rgba(241,199,33,.06);
}}
.hero-eyebrow .brand-icon{{ width:18px; height:18px; }}
.hero-copy h1{{ font-family:var(--font-display); font-weight:800; font-size:clamp(36px,5vw,58px); line-height:1.04; margin:0 0 20px; letter-spacing:-1.5px; color:var(--text); }}
.hero-copy h1 em{{ font-style:normal; color:var(--yellow); }}
.hero-copy p{{ color:var(--text-dim); font-size:17.5px; max-width:560px; margin:0 0 32px; }}
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
  .hero{{ padding:118px 0 64px; }}
}}

/* ---------- TOOLBAR: BUSCADOR + ASISTENTE ---------- */
.toolbar{{
  position:sticky; top:96px; z-index:90;
  padding:14px 0; transition:top .2s ease;
}}
.toolbar-wrap{{ position:relative; }}
.toolbar-inner{{
  display:flex; gap:10px; align-items:center; flex-wrap:wrap;
  background:rgba(18,17,15,.78);
  border:1px solid var(--line-amber);
  border-radius:20px;
  padding:9px 10px;
  backdrop-filter:blur(18px) saturate(1.15);
  -webkit-backdrop-filter:blur(18px) saturate(1.15);
  box-shadow:0 18px 44px rgba(0,0,0,.5), 0 0 0 1px rgba(255,255,255,.03) inset;
}}
.search-box{{
  flex:1 1 260px; position:relative; display:flex; align-items:center;
  background:transparent; border:none; border-radius:14px;
  padding:0 6px 0 12px; transition:background .15s;
}}
.search-box:focus-within{{ background:rgba(255,255,255,.05); }}
.search-box svg{{ flex:none; color:var(--text-faint); }}
.search-box input{{
  flex:1; border:none; background:transparent; outline:none;
  font-family:var(--font-body); font-size:14.5px; color:var(--text); padding:12px 10px;
}}
.search-box input::placeholder{{ color:var(--text-faint); }}
.search-clear{{
  flex:none; display:none; align-items:center; justify-content:center; width:26px; height:26px;
  border:none; border-radius:50%; background:rgba(255,255,255,.08); color:var(--text-dim); cursor:pointer; font-size:12px;
}}
.search-clear:hover{{ background:rgba(255,255,255,.14); }}
.search-count{{ font-size:11.5px; color:var(--text-faint); font-weight:600; padding:0 10px 0 2px; white-space:nowrap; }}

/* Sugerencias de búsqueda (antes y mientras escribe) */
.search-suggest{{
  position:absolute; top:calc(100% + 8px); left:0; right:0; z-index:80;
  background:rgba(18,17,15,.95); border:1px solid var(--line-amber); border-radius:16px;
  padding:10px; max-height:380px; overflow-y:auto;
  box-shadow:0 20px 48px rgba(0,0,0,.5);
  backdrop-filter:blur(18px) saturate(1.1); -webkit-backdrop-filter:blur(18px) saturate(1.1);
  opacity:0; visibility:hidden; transform:translateY(-6px); pointer-events:none;
  transition:opacity .18s ease, transform .18s ease, visibility 0s linear .18s;
}}
.search-suggest.is-open{{ opacity:1; visibility:visible; transform:translateY(0); pointer-events:auto; transition:opacity .18s ease, transform .18s ease; }}
.suggest-label{{ font-size:10.5px; font-weight:800; text-transform:uppercase; letter-spacing:.07em; color:var(--text-faint); padding:6px 8px 10px; }}
.suggest-chips{{ display:flex; flex-wrap:wrap; gap:8px; padding:0 6px 4px; }}
.suggest-chip{{
  background:rgba(255,255,255,.06); border:1px solid rgba(255,255,255,.14); color:rgba(255,255,255,.78);
  font-size:12.5px; font-weight:700; padding:8px 14px; border-radius:999px; cursor:pointer;
  transition:color .18s ease, border-color .18s ease, background .18s ease;
}}
.suggest-chip:hover{{ background:rgba(241,199,33,.14); border-color:var(--yellow); color:var(--yellow); }}
.suggest-list{{ display:flex; flex-direction:column; gap:3px; }}
.suggest-item{{
  display:flex; align-items:center; justify-content:space-between; gap:12px;
  padding:11px 12px; border-radius:11px; text-decoration:none; color:var(--text);
  transition:background .15s ease;
}}
.suggest-item:hover{{ background:rgba(241,199,33,.08); }}
.suggest-item b{{ font-weight:700; font-size:13.5px; line-height:1.3; }}
.suggest-item .tag{{ flex:none; font-size:10.5px; color:var(--text-faint); font-weight:700; white-space:nowrap; padding:3px 9px; border-radius:999px; background:rgba(255,255,255,.06); }}
.suggest-empty{{ padding:18px 10px; text-align:center; color:var(--text-faint); font-size:13px; }}

.assistant-toggle{{
  flex:0 0 auto; display:inline-flex; align-items:center; gap:9px;
  background:var(--yellow); color:var(--ink); border:none; border-radius:15px;
  padding:9px 18px 9px 9px; cursor:pointer; font-family:var(--font-body); font-weight:800; font-size:13.5px;
  transition:transform .12s ease, box-shadow .12s ease, background .12s ease;
}}
.assistant-toggle:hover{{ box-shadow:0 8px 22px rgba(241,199,33,.4); transform:translateY(-1px); background:var(--yellow-50); }}
.assistant-toggle .brand-icon{{ width:26px; height:26px; }}
.assistant-toggle .at-dot{{ width:7px; height:7px; border-radius:50%; background:#1E8A44; box-shadow:0 0 0 3px rgba(30,138,68,.25); }}

@media (max-width:720px){{ .toolbar{{ top:84px; }} }}

.no-results{{ display:none; text-align:center; padding:60px 20px; color:var(--text-dim); }}
.no-results .brand-icon{{ width:64px; height:64px; margin:0 auto 14px; opacity:.7; }}
.no-results h3{{ font-size:19px; margin-bottom:6px; color:var(--text); }}
.no-results p{{ font-size:14px; margin:0; }}
.is-hidden{{ display:none !important; }}

/* Chat panel: overlay flotante, no empuja el resto de la página */
.chat-panel{{
  position:absolute; top:100%; left:0; right:0; margin-top:10px;
  max-height:0; overflow:hidden; opacity:0; visibility:hidden;
  transition:max-height .32s ease, opacity .25s ease, visibility 0s linear .32s;
  z-index:95;
}}
.chat-panel.is-open{{ max-height:640px; opacity:1; visibility:visible; transition:max-height .32s ease, opacity .25s ease; }}
.chat-shell{{
  background:var(--bg); border:1px solid var(--line-amber); border-radius:var(--radius-lg); overflow:hidden; box-shadow:var(--shadow-lg);
  display:flex; flex-direction:column; max-width:640px;
}}
.chat-head{{ display:flex; align-items:center; gap:10px; padding:16px 18px; border-bottom:1px solid var(--line); }}
.chat-head .brand-icon{{ width:32px; height:32px; }}
.chat-head b{{ display:block; font-family:var(--font-display); font-size:14px; color:var(--text); }}
.chat-head small{{ color:var(--text-faint); font-size:11.5px; }}
.chat-close{{ margin-left:auto; background:none; border:none; color:var(--text-dim); opacity:.7; cursor:pointer; font-size:18px; line-height:1; padding:4px; }}
.chat-close:hover{{ opacity:1; }}
.chat-body{{ padding:18px; display:flex; flex-direction:column; gap:12px; max-height:340px; overflow-y:auto; background:var(--bg-alt); }}
.chat-msg{{ display:flex; gap:10px; max-width:88%; }}
.chat-msg.user{{ align-self:flex-end; flex-direction:row-reverse; }}
.chat-msg .bubble{{
  background:var(--paper-50); color:var(--ink); border-radius:14px 14px 14px 4px; padding:10px 14px;
  font-size:13.5px; line-height:1.5;
}}
.chat-msg.user .bubble{{ background:var(--yellow); border-radius:14px 14px 4px 14px; font-weight:600; }}
.chat-msg .avatar{{ width:26px; height:26px; flex:none; border-radius:50%; background-color:var(--yellow); padding:4px; box-sizing:border-box; }}
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
  background:rgba(255,255,255,.06); border:1px solid rgba(255,255,255,.14); color:var(--text-dim);
  font-size:12px; font-weight:600; padding:7px 13px; border-radius:var(--radius-pill); cursor:pointer;
}}
.chat-chip:hover{{ background:rgba(241,199,33,.16); border-color:var(--yellow); color:var(--yellow); }}
.chat-input-row{{ display:flex; gap:8px; padding:14px 18px; border-top:1px solid var(--line); }}
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
.cat-section{{ padding:72px 0; border-bottom:1px solid var(--line); scroll-margin-top:200px; }}
.cat-section:nth-of-type(even){{ background:var(--bg-alt); }}
.cat-section:last-of-type{{ border-bottom:none; }}
.cat-head{{ max-width:680px; margin-bottom:34px; }}
.cat-eyebrow{{
  font-family:var(--font-body); font-weight:700; font-size:12px; letter-spacing:.08em;
  text-transform:uppercase; color:var(--yellow); margin:0 0 10px; display:flex; align-items:center; gap:8px;
}}
.cat-eyebrow .dot{{ width:7px; height:7px; border-radius:50%; background:var(--yellow); box-shadow:0 0 8px rgba(241,199,33,.6); }}
.cat-head h2{{ font-family:var(--font-display); font-weight:800; font-size:clamp(28px,3.4vw,38px); margin:0 0 12px; letter-spacing:-.8px; color:var(--text); }}
.cat-head p{{ color:var(--text-dim); font-size:15.5px; margin:0; }}

.level-nav{{ display:flex; gap:10px; flex-wrap:wrap; margin-bottom:44px; }}
.level-pill{{
  --nivel-accent: var(--yellow);
  display:inline-flex; align-items:center; gap:8px;
  background:var(--surface); border:1.5px solid var(--line); text-decoration:none; color:var(--text);
  font-family:var(--font-body); font-weight:700; font-size:13.5px;
  padding:10px 18px; border-radius:var(--radius-pill); transition:.15s;
}}
.level-pill:hover{{ border-color:var(--nivel-accent); box-shadow:0 4px 18px rgba(0,0,0,.35); transform:translateY(-1px); }}
.level-pill span{{ background:var(--nivel-accent); color:var(--ink); font-size:11.5px; padding:2px 8px; border-radius:var(--radius-pill); font-weight:800; }}

.nivel-block{{ margin-bottom:8px; scroll-margin-top:200px; }}
.nivel-head{{ display:flex; align-items:center; gap:14px; margin:0 0 26px; }}
.nivel-chip{{
  --nivel-accent: var(--yellow);
  font-family:var(--font-display); font-weight:700; font-size:17px;
  color:var(--text); display:flex; align-items:center; gap:8px;
  padding-bottom:4px; border-bottom:3px solid var(--nivel-accent);
}}
.nivel-line{{ flex:1; height:1px; background:var(--line); }}
.nivel-total{{ font-size:12.5px; color:var(--text-faint); font-weight:600; white-space:nowrap; }}

.module-group{{ margin-bottom:40px; scroll-margin-top:200px; }}
.module-head{{ display:flex; align-items:baseline; gap:12px; margin-bottom:16px; flex-wrap:wrap; }}
.module-tag{{
  font-family:var(--font-display); font-weight:800; font-size:12px;
  background:var(--yellow); color:var(--ink); padding:4px 10px; border-radius:7px; letter-spacing:.02em;
}}
.module-tag--otros{{ background:var(--red); color:var(--white); }}
.module-name{{ font-size:18px; font-weight:700; letter-spacing:-.2px; color:var(--text); }}
.module-count{{ font-size:12px; color:var(--text-faint); font-weight:600; margin-left:auto; }}

/* ---------- CARDS / CARRUSEL ---------- */
.carousel{{ position:relative; }}
.card-grid{{
  display:flex; flex-wrap:nowrap; gap:16px;
  overflow-x:auto; scroll-snap-type:x mandatory; -webkit-overflow-scrolling:touch;
  scrollbar-width:none; -ms-overflow-style:none;
  padding:4px 36px 8px; scroll-padding:0 36px;
}}
.card-grid::-webkit-scrollbar{{ display:none; }}
.class-card{{ flex:0 0 296px; scroll-snap-align:start; }}

.car-arrow{{
  position:absolute; top:44%; transform:translateY(-50%); z-index:5;
  width:38px; height:38px; border-radius:50%; display:flex; align-items:center; justify-content:center;
  background:rgba(17,16,14,.86); border:1px solid var(--line-amber); color:var(--yellow);
  cursor:pointer; box-shadow:0 8px 20px rgba(0,0,0,.5); padding:0;
  transition:opacity .2s ease, background .2s ease, transform .2s ease;
}}
.car-arrow:hover{{ background:rgba(241,199,33,.16); }}
.car-arrow:disabled{{ opacity:.22; pointer-events:none; }}
.car-prev{{ left:-10px; }}
.car-next{{ right:-10px; }}

.car-dots{{ display:flex; justify-content:center; align-items:center; gap:6px; margin-top:14px; }}
.car-dot{{ width:6px; height:6px; border-radius:999px; background:rgba(255,255,255,.18); transition:background .2s ease, width .2s ease; }}
.car-dot.is-active{{ background:var(--yellow); width:18px; }}
.class-card{{
  --nivel-accent: var(--yellow);
  display:block; text-decoration:none; color:var(--text);
  background:var(--surface); border:1px solid var(--line); border-top:4px solid var(--nivel-accent);
  border-radius:var(--radius-md); padding:20px 20px 18px;
  box-shadow:var(--shadow-sm);
  transition:box-shadow .18s ease, transform .18s ease, border-color .18s ease, background .18s ease;
  position:relative;
}}
.class-card:hover{{ box-shadow:var(--shadow-md), 0 0 0 1px var(--nivel-accent) inset; border-color:var(--nivel-accent); background:var(--surface-strong); transform:translateY(-3px); }}
.class-card--soon{{ cursor:default; opacity:.55; }}
.class-card--soon:hover{{ transform:none; box-shadow:var(--shadow-sm); border-color:var(--line); background:var(--surface); }}
.cc-top{{ display:flex; align-items:center; justify-content:space-between; gap:8px; margin-bottom:12px; }}
.cc-num{{ font-family:var(--font-display); font-weight:700; font-size:11.5px; color:var(--text-faint); letter-spacing:.03em; }}
.badge{{
  display:inline-flex; align-items:center; gap:5px;
  font-size:10.5px; font-weight:700; padding:4px 10px; border-radius:var(--radius-pill);
  font-family:var(--font-body); white-space:nowrap;
}}
.badge-dot{{ width:5px; height:5px; border-radius:50%; }}
.badge-yellow{{ background:rgba(241,199,33,.14); color:var(--yellow); }}
.badge-yellow .badge-dot{{ background:var(--yellow); }}
.badge-red{{ background:rgba(219,0,0,.18); color:#FF8A8A; }}
.badge-red .badge-dot{{ background:var(--red); }}
.badge-ink{{ background:rgba(167,139,250,.16); color:var(--violet); }}
.badge-ink .badge-dot{{ background:var(--violet); }}
.cc-title{{ font-family:var(--font-display); font-size:15.5px; font-weight:700; line-height:1.32; margin:0 0 8px; letter-spacing:-.1px; color:var(--text); }}
.cc-desc{{ font-size:13px; color:var(--text-dim); margin:0 0 16px; line-height:1.5; }}
.cc-foot{{ display:flex; align-items:center; }}
.cc-play{{ display:inline-flex; align-items:center; gap:6px; font-size:12.5px; font-weight:700; color:var(--yellow); }}
.class-card:hover .cc-play{{ text-decoration:underline; }}
.cc-soon{{ font-size:12px; font-weight:700; color:var(--text-faint); text-transform:uppercase; letter-spacing:.04em; }}

/* ---------- FOOTER ---------- */
.site-footer{{ background:var(--bg-alt); color:var(--text-dim); padding:44px 0; border-top:1px solid var(--line); }}
.footer-inner{{ display:flex; align-items:center; justify-content:space-between; gap:20px; flex-wrap:wrap; }}
.footer-brand{{ display:flex; align-items:center; gap:10px; }}
.footer-brand .brand-icon{{ width:24px; height:24px; }}
.footer-brand span{{ font-family:var(--font-display); font-weight:700; font-size:14px; color:var(--text); }}
.site-footer p{{ margin:0; font-size:12.5px; opacity:.75; }}

@media (max-width:640px){{
  .wrap{{ padding:0 20px; }}
  .card-grid{{
    gap:14px; margin:0 -20px; padding:4px 20px 14px; scroll-padding:0 20px;
  }}
  .class-card{{ flex:0 0 82vw; max-width:340px; }}
  .car-arrow{{ width:34px; height:34px; }}
  .car-prev{{ left:2px; }}
  .car-next{{ right:2px; }}
  .car-dots{{ margin-top:4px; }}
}}
</style>
</head>
<body>

<nav class="nav" id="siteNav">
  <div class="nav-inner">
    <a class="nav-brand" href="#top">
      <span class="brand-icon" role="img" aria-label="Llamaleads"></span>
      <div><span>LlamaLeads Academy</span><small>Capacitación CRM Llamaleads</small></div>
    </a>
    <button class="nav-toggle" id="navToggle" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="navMenu">
      <span></span><span></span><span></span>
    </button>
  </div>
  <ul class="nav-menu" id="navMenu">
    {NAV_HTML}
  </ul>
</nav>

<header class="hero" id="top">
  <div class="flame-orb"></div>
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
  <div class="wrap toolbar-wrap">
    <div class="toolbar-inner">
      <div class="search-box">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="7" cy="7" r="5.5" stroke="currentColor" stroke-width="1.6"/><path d="M11.5 11.5L15 15" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
        <input type="text" id="searchInput" placeholder="¿Qué quieres aprender?" autocomplete="off">
        <span class="search-count" id="searchCount"></span>
        <button class="search-clear" id="searchClear" type="button" aria-label="Limpiar búsqueda">✕</button>
        <div class="search-suggest" id="searchSuggest"></div>
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

/* ---------------- Carruseles de clases (mobile) ---------------- */
(function() {{
  document.querySelectorAll('.module-group').forEach(group => {{
    const grid = group.querySelector('.card-grid');
    const prev = group.querySelector('.car-prev');
    const next = group.querySelector('.car-next');
    const dots = Array.from(group.querySelectorAll('.car-dot'));
    if (!grid || !dots.length) return;

    function step() {{
      const cards = grid.querySelectorAll('.class-card');
      if (cards.length > 1) {{
        return cards[1].offsetLeft - cards[0].offsetLeft;
      }}
      return grid.clientWidth;
    }}

    function activeIndex() {{
      const maxScroll = grid.scrollWidth - grid.clientWidth;
      if (maxScroll <= 1) return 0;
      const frac = grid.scrollLeft / maxScroll;
      return Math.round(frac * (dots.length - 1));
    }}

    function refresh() {{
      const idx = Math.max(0, Math.min(dots.length - 1, activeIndex()));
      dots.forEach((d, i) => d.classList.toggle('is-active', i === idx));
      if (prev) prev.disabled = grid.scrollLeft <= 4;
      if (next) next.disabled = grid.scrollLeft >= grid.scrollWidth - grid.clientWidth - 4;
    }}

    if (prev) prev.addEventListener('click', () => {{
      grid.scrollBy({{ left: -step(), behavior: 'smooth' }});
    }});
    if (next) next.addEventListener('click', () => {{
      grid.scrollBy({{ left: step(), behavior: 'smooth' }});
    }});

    let ticking = false;
    grid.addEventListener('scroll', () => {{
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => {{ refresh(); ticking = false; }});
    }});

    window.addEventListener('resize', refresh);
    refresh();
  }});
}})();

/* ---------------- Menú hamburguesa del navbar ---------------- */
(function() {{
  const nav = document.getElementById('siteNav');
  const toggle = document.getElementById('navToggle');
  const menu = document.getElementById('navMenu');
  if (!nav || !toggle || !menu) return;

  function setOpen(open) {{
    nav.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
  }}

  toggle.addEventListener('click', (e) => {{
    e.stopPropagation();
    setOpen(!nav.classList.contains('is-open'));
  }});

  menu.querySelectorAll('a').forEach(a => {{
    a.addEventListener('click', () => setOpen(false));
  }});

  document.addEventListener('click', (e) => {{
    if (!nav.contains(e.target)) setOpen(false);
  }});

  document.addEventListener('keydown', (e) => {{
    if (e.key === 'Escape') setOpen(false);
  }});

  /* Acordeón por categoría: cada botón despliega solo sus módulos */
  menu.querySelectorAll('.nav-cat').forEach(cat => {{
    const catToggle = cat.querySelector('.nav-cat-toggle');
    if (!catToggle) return;
    catToggle.addEventListener('click', (e) => {{
      e.stopPropagation();
      const willOpen = !cat.classList.contains('is-open');
      cat.classList.toggle('is-open', willOpen);
      catToggle.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
    }});
  }});
}})();

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

  /* ---- Sugerencias: chips (vacío) + resultados en vivo (escribiendo) ---- */
  const suggestBox = document.getElementById('searchSuggest');

  function escapeHtml(s) {{
    const d = document.createElement('div');
    d.textContent = s == null ? '' : s;
    return d.innerHTML;
  }}

  function moduleLabel(m) {{
    if (!m) return '';
    if (m.includes('·')) return m.split('·')[1].trim();
    if (m.startsWith('M_')) return m.slice(2).trim();
    return m;
  }}

  const MODULES = [];
  const seenMods = new Set();
  COURSES.forEach(c => {{
    const label = moduleLabel(c.modulo);
    if (label && !seenMods.has(label)) {{ seenMods.add(label); MODULES.push(label); }}
  }});

  function norm(s) {{ return (s || '').toLowerCase(); }}

  function searchCourses(q) {{
    const terms = norm(q).split(/\\s+/).filter(Boolean);
    if (!terms.length) return [];
    const matched = COURSES.filter(c => {{
      const blob = norm(c.titulo + ' ' + c.desc + ' ' + c.modulo);
      return terms.every(t => blob.includes(t));
    }});
    matched.sort((a, b) => {{
      const aHit = norm(a.titulo).includes(norm(q)) ? 0 : 1;
      const bHit = norm(b.titulo).includes(norm(q)) ? 0 : 1;
      return aHit - bHit;
    }});
    return matched.slice(0, 6);
  }}

  function renderChips() {{
    const chips = MODULES.map(m =>
      '<button type="button" class="suggest-chip">' + escapeHtml(m) + '</button>'
    ).join('');
    suggestBox.innerHTML = '<div class="suggest-label">Sugerencias</div><div class="suggest-chips">' + chips + '</div>';
    suggestBox.querySelectorAll('.suggest-chip').forEach(chip => {{
      chip.addEventListener('click', (ev) => {{
        ev.stopPropagation();
        input.value = chip.textContent;
        input.dispatchEvent(new Event('input', {{ bubbles: true }}));
        input.focus();
      }});
    }});
  }}

  function renderResults(list, q) {{
    if (!list.length) {{
      suggestBox.innerHTML = '<div class="suggest-empty">No encontramos clases para "' + escapeHtml(q) + '". Probá con otra palabra 🦙</div>';
      return;
    }}
    const items = list.map(c => {{
      const tag = c.clase ? ('Clase ' + c.clase) : (moduleLabel(c.modulo) || 'Workflow');
      if (c.video) {{
        return '<a class="suggest-item" href="' + c.video + '" target="_blank" rel="noopener"><b>' + escapeHtml(c.titulo) + '</b><span class="tag">' + escapeHtml(tag) + '</span></a>';
      }}
      return '<div class="suggest-item" style="opacity:.55;cursor:default;"><b>' + escapeHtml(c.titulo) + '</b><span class="tag">Próximamente</span></div>';
    }}).join('');
    suggestBox.innerHTML = '<div class="suggest-label">Coincidencias</div><div class="suggest-list">' + items + '</div>';
  }}

  function updateSuggest() {{
    const q = input.value.trim();
    if (!q) renderChips();
    else renderResults(searchCourses(q), q);
  }}

  function openSuggest() {{ suggestBox.classList.add('is-open'); }}
  function closeSuggest() {{ suggestBox.classList.remove('is-open'); }}

  input.addEventListener('focus', () => {{ updateSuggest(); openSuggest(); }});
  input.addEventListener('input', () => {{ updateSuggest(); openSuggest(); }});
  suggestBox.addEventListener('click', (e) => {{
    if (e.target.closest('a.suggest-item')) closeSuggest();
  }});
  document.addEventListener('click', (e) => {{
    if (!e.target.closest('.search-box')) closeSuggest();
  }});
  document.addEventListener('keydown', (e) => {{
    if (e.key === 'Escape') closeSuggest();
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
