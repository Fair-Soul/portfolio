# AezakmiSO demo-screen kit: generates HTML screens (1200 css px wide) with demo data.
import math, random, os
random.seed(7)
import os
F = 'file://' + os.path.abspath(os.path.join(os.path.dirname(__file__), '../../fonts')) + '/'
CSS = f"""
@font-face{{font-family:G;src:url({F}golos-text-latin-400-normal.woff2);font-weight:400;unicode-range:U+0000-024F,U+2000-22FF}}
@font-face{{font-family:G;src:url({F}golos-text-cyrillic-400-normal.woff2);font-weight:400;unicode-range:U+0400-04FF}}
@font-face{{font-family:G;src:url({F}golos-text-latin-600-normal.woff2);font-weight:600 900;unicode-range:U+0000-024F,U+2000-22FF}}
@font-face{{font-family:G;src:url({F}golos-text-cyrillic-600-normal.woff2);font-weight:600;unicode-range:U+0400-04FF}}
@font-face{{font-family:G;src:url({F}golos-text-cyrillic-800-normal.woff2);font-weight:800;unicode-range:U+0400-04FF}}
@font-face{{font-family:G;src:url({F}golos-text-cyrillic-900-normal.woff2);font-weight:900;unicode-range:U+0400-04FF}}
@font-face{{font-family:GH;src:url({F}golos-text-cyrillic-800-normal.woff2);font-weight:800}}
@font-face{{font-family:GH;src:url({F}golos-text-cyrillic-900-normal.woff2);font-weight:900}}
@font-face{{font-family:A;src:url({F}archivo.woff2)}}
:root{{--bg:#0C0E0F;--s:#15181A;--s2:#1B1F22;--ln:#252A2E;--ink:#E8EDF1;--mu:#81878D;--ac:#FF4D29;--mine:#30140F;--ok:#49E2A0;--wa:#E9BF42;--bad:#E26C82;--side:#08090A}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1200px;background:var(--bg);color:var(--ink);font:13px/1.45 G,sans-serif;-webkit-font-smoothing:antialiased}}
.app{{display:grid;grid-template-columns:212px 1fr;min-height:750px}}
.side{{background:var(--side);border-right:1px solid var(--ln);padding:18px 14px;position:relative;overflow:hidden}}
.logo{{display:flex;align-items:center;gap:6px;font:italic 900 19px/1 A,GH,G;letter-spacing:-.5px;margin-bottom:18px}}
.logo i{{background:var(--ac);color:#000;font:800 9px/1 GH,G;padding:3px 4px;border-radius:3px;font-style:normal}}
.cmd{{height:28px;border:1px solid var(--ln);border-radius:7px;color:var(--mu);font-size:11px;display:flex;align-items:center;padding:0 9px;margin-bottom:16px;justify-content:space-between}}
.grp{{font:600 9.5px/1 G;letter-spacing:1.2px;color:#5d6368;text-transform:uppercase;margin:14px 6px 6px}}
.nv{{display:flex;align-items:center;gap:8px;padding:7px 8px;border-radius:7px;color:#b9c0c6;font-size:12px;white-space:nowrap}}
.nv svg{{width:14px;height:14px;stroke:currentColor;fill:none;stroke-width:1.7;opacity:.8}}
.nv.on{{background:var(--s2);color:var(--ink);box-shadow:inset 2px 0 0 var(--ac)}}
.nv b{{margin-left:auto;font:600 10px/1 G;background:var(--s2);color:var(--mu);padding:3px 6px;border-radius:9px}}
.nv b.r{{background:var(--ac);color:#000}}
.bolt{{position:absolute;left:-30px;bottom:170px;width:250px;opacity:.09}}
.chk{{position:absolute;left:14px;right:14px;bottom:18px}}
.chk p{{font-size:10.5px;color:var(--mu);margin-bottom:7px}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:6px;height:30px;padding:0 12px;border-radius:7px;font:600 12px/1 G;background:var(--s2);border:1px solid var(--ln);color:var(--ink)}}
.btn.p{{background:var(--ac);border-color:var(--ac);color:#140603}}
.main{{padding:22px 28px 36px;min-width:0}}
.hd{{display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:16px}}
h1{{font:900 30px/1 GH,G;text-transform:uppercase;letter-spacing:-.3px}}
.meta{{color:var(--mu);font-size:11.5px}}
.fb{{display:flex;gap:14px;align-items:flex-end;margin-bottom:18px}}
.fb label{{display:block;font-size:10px;color:var(--mu);margin-bottom:5px}}
.sel{{height:30px;border:1px solid var(--ln);border-radius:7px;background:var(--s);display:flex;align-items:center;padding:0 10px;gap:20px;font-size:12px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.seg{{display:flex;border:1px solid var(--ln);border-radius:7px;overflow:hidden;background:var(--s)}}
.seg span{{padding:0 11px;height:28px;display:flex;align-items:center;font-size:12px;color:#b9c0c6;gap:5px}}
.seg span.on{{background:var(--ink);color:#0C0E0F;font-weight:600}}
.fl{{font-size:11px}}
.card{{background:var(--s);border:1px solid var(--ln);border-radius:11px}}
.sec{{margin-top:22px}}
.st{{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px}}
.st h2{{font:800 12.5px/1 GH,G;text-transform:uppercase;letter-spacing:.6px}}
.st a{{font-size:11px;color:var(--mu)}}
.kpis{{display:grid;grid-template-columns:1.25fr 1fr 1fr 1fr;gap:12px}}
.kpi{{padding:16px;min-height:112px;position:relative;overflow:hidden}}
.kpi .l{{font-size:11.5px;color:var(--mu)}}
.kpi .v{{font:800 32px/1 GH,G;margin:12px 0 8px;letter-spacing:-.5px;display:flex;align-items:baseline;gap:6px}}
.kpi .v small{{font:600 15px/1 G;letter-spacing:0}}
.kpi .l,.kpi .d{{position:relative;z-index:1}}

.kpi .d{{font-size:11px;color:var(--mu)}}
.kpi.o{{background:var(--ac);border-color:var(--ac);color:#140603}}
.kpi.o .l,.kpi.o .d{{color:#4a1408}}
.kpi.o svg{{position:absolute;right:14px;top:14px;width:40px;fill:#140603;opacity:.9}}
.up{{color:var(--ok)}} .dn{{color:var(--bad)}} .wa{{color:var(--wa)}}
.ic{{width:30px;height:30px;border-radius:8px;flex:none;display:grid;place-items:center}}
.ic svg{{width:16px;height:16px;fill:none;stroke:#fff;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}}
.ic.sm{{width:24px;height:24px;border-radius:6px}} .ic.sm svg{{width:13px;height:13px}}
.ic.lg{{width:64px;height:64px;border-radius:15px}} .ic.lg svg{{width:30px;height:30px}}
.row{{display:flex;align-items:center;gap:11px;padding:10px 14px;border-top:1px solid var(--ln)}}
.row:first-child{{border-top:0}}
.nm{{font-weight:600;font-size:12.5px}} .sb{{font-size:11px;color:var(--mu)}}
.tag{{font:600 9.5px/1 G;color:var(--ac);background:#3a150d;padding:3px 5px;border-radius:4px;margin-left:6px;vertical-align:1px}}
.chips{{display:flex;flex-wrap:wrap;gap:6px;margin-left:auto;max-width:640px;justify-content:flex-end}}
.chip{{display:flex;align-items:center;gap:6px;border:1px solid var(--ln);border-radius:7px;padding:4px 6px 4px 8px;font-size:11px;background:var(--s2)}}
.pos{{min-width:20px;height:18px;border-radius:5px;background:#2b3135;font:700 10.5px/18px G;text-align:center;padding:0 4px}}
.pos.t{{background:var(--ink);color:#0C0E0F}} .pos.o{{background:var(--ac);color:#140603}}
.dl{{font:600 10px/1 G}}
.mine{{background:linear-gradient(90deg,rgba(255,77,41,.10),rgba(255,77,41,.03));box-shadow:inset 3px 0 0 var(--ac)}}
.mv{{margin-left:auto;display:flex;align-items:center;gap:7px;font-size:11px;color:var(--mu)}}
.when{{font-size:11px;color:var(--mu);width:90px;text-align:right}}
.flag{{font-size:9.5px;font-weight:600;color:var(--mu);border:1px solid var(--ln);border-radius:4px;padding:1px 4px;margin:0 2px}}
.tbl{{width:100%;border-collapse:collapse;font-size:12px}}
.tbl th{{text-align:left;font-weight:400;color:var(--mu);font-size:10.5px;padding:9px 14px;border-bottom:1px solid var(--ln)}}
.tbl td{{padding:9px 14px;border-top:1px solid var(--ln)}}
.tbl tr:first-child td{{border-top:0}}
.r{{text-align:right!important;white-space:nowrap}} .nw{{white-space:nowrap}}
.bar{{height:5px;border-radius:3px;background:#2b3135;position:relative;width:90px;display:inline-block;vertical-align:middle}}
.bar i{{position:absolute;left:0;top:0;bottom:0;border-radius:3px;background:var(--bad)}}
.tabs{{display:flex;gap:4px;border-bottom:1px solid var(--ln);margin:18px 0 16px}}
.tabs span{{padding:9px 12px;font-size:12.5px;color:var(--mu)}}
.tabs span.on{{color:var(--ink);box-shadow:inset 0 -2px 0 var(--ac)}}
.badge{{font:600 10px/1 G;padding:4px 7px;border-radius:5px;border:1px solid;white-space:nowrap;flex:none}}
.badge.ok{{color:var(--ok);border-color:#1f5a41;background:#0f241b}}
.badge.wa{{color:var(--wa);border-color:#5d4c1a;background:#241e0c}}
.g2{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}
.g3{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}}
.pad{{padding:16px}}
.shot{{width:62px;height:112px;border-radius:9px;position:relative;overflow:hidden;flex:none}}
.shot b{{position:absolute;left:7px;right:7px;top:9px;height:6px;border-radius:3px;background:rgba(255,255,255,.9)}}
.shot b+b{{top:19px;right:20px;height:4px;background:rgba(255,255,255,.55)}}
.shot s{{position:absolute;left:8px;right:8px;top:32px;bottom:10px;border-radius:6px;background:rgba(255,255,255,.92);box-shadow:0 4px 10px rgba(0,0,0,.25)}}
.shot s:after{{content:"";position:absolute;left:6px;right:6px;top:7px;height:4px;border-radius:2px;background:#d9dde1;box-shadow:0 8px 0 #e6e9ec,0 16px 0 #e6e9ec,0 24px 0 #e6e9ec}}
.shot u{{position:absolute;left:14px;right:14px;bottom:16px;height:14px;border-radius:5px}}
"""
BOLT = '<svg viewBox="0 0 100 160"><path d="M62 0 L8 92 H44 L30 160 L92 58 H56 Z"/></svg>'
I = {  # icon glyphs
 'doc':'<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/>',
 'pen':'<path d="M4 20l4-1 11-11-3-3L5 16z"/><path d="M14 6l3 3"/>',
 'scan':'<path d="M4 8V4h4M20 8V4h-4M4 16v4h4M20 16v4h-4M4 12h16"/>',
 'cam':'<rect x="3" y="7" width="18" height="13" rx="3"/><circle cx="12" cy="13.5" r="3.5"/><path d="M9 7l1.5-3h3L15 7"/>',
 'shield':'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 'globe':'<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c3 3 3 14 0 17M12 3.5c-3 3-3 14 0 17"/>',
 'grid':'<rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="4" width="7" height="7" rx="1.5"/><rect x="4" y="13" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/>',
 'spark':'<path d="M12 3v5M12 16v5M3 12h5M16 12h5M6 6l3 3M15 15l3 3M18 6l-3 3M9 15l-3 3"/>',
}
GR = [('#FF6A3D','#C2185B'),('#7B61FF','#3D2BB8'),('#22C1A3','#0E7C86'),('#F7B733','#E8603C'),('#3FA9F5','#2D5BD9'),('#E04E8A','#7A2BB5'),('#5BD06B','#1C8F5A'),('#FF8A65','#D84315'),('#8E9BFF','#5160E0'),('#2ED3C6','#1E7FD9')]
def icon(kind, g, cls=''):
    a,b = GR[g % len(GR)]
    return f'<span class="ic {cls}" style="background:linear-gradient(140deg,{a},{b})"><svg viewBox="0 0 24 24">{I[kind]}</svg></span>'
def shot(g, k=0):
    a,b = GR[g % len(GR)]
    ang = 160 + k*25
    u = ['#FF4D29','#2D5BD9','#1C8F5A','#7A2BB5'][ (g+k) % 4]
    return f'<span class="shot" style="background:linear-gradient({ang}deg,{a},{b})"><b></b><b></b><s></s><u style="background:{u}"></u></span>'
NAV = [('МОЁ',[('Сводка','home',''),('Мои приложения','grid','2'),('Тексты','doc','r2')]),
       ('РЫНОК',[('Позиции и выдача','scan',''),('Все приложения','grid',''),('Лента изменений','spark','14')]),
       ('АНАЛИТИКА',[('Ниша и сроки жизни','chart',''),('Прогнозы и модели','trend',''),('Тренды','globe','')])]
NI = {'home':'<path d="M4 11l8-7 8 7v9H4z"/>','chart':'<path d="M4 20V4M4 20h16M8 16v-5M12 16V8M16 16v-3"/>','trend':'<path d="M4 17l5-5 4 3 7-8"/><path d="M15 7h5v5"/>'}
def side(active):
    h = f'<aside class="side" id="nav"><div class="logo">AEZAKMI <i>SO</i></div><div class="cmd">Команда <span>⌘K</span></div>'
    for g,items in NAV:
        h += f'<div class="grp">{g}</div>'
        for n,ic,c in items:
            svg = NI.get(ic) or I.get(ic)
            b = ''
            if c: b = f'<b class="r">{c[1:]}</b>' if c.startswith('r') else f'<b>{c}</b>'
            h += f'<div class="nv{" on" if n==active else ""}"><svg viewBox="0 0 24 24">{svg}</svg>{n}{b}</div>'
    h += f'<div class="nv" style="margin-top:14px"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/></svg>Настройка</div>'
    h += '<div class="chk"><p>Проверено 40 мин назад</p><div class="btn p" style="width:100%">Проверить сейчас</div></div></aside>'
    return h
def filt(extra=''):
    return f'''<div class="fb" id="filter"><div><label>Ключ</label><div class="sel">Все ключи <span>▾</span></div></div>
<div><label>Страна</label><div class="seg"><span class="on">Все</span><span>BR</span><span>DE</span><span>US</span></div></div>
<div><label>Стор</label><div class="seg"><span class="on">Оба</span><span>App Store</span><span>Google Play</span></div></div>{extra}</div>'''
def page(active, body, title='AezakmiSO'):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="app">{side(active)}<main class="main">{body}</main></div></body></html>'

def path(pts, w, h, lo, hi, smooth=True):
    n=len(pts); xs=[i*w/(n-1) for i in range(n)]; ys=[h-(p-lo)/(hi-lo)*h for p in pts]
    d=f'M{xs[0]:.1f},{ys[0]:.1f}'
    for i in range(1,n):
        cx=(xs[i-1]+xs[i])/2
        d+=f' C{cx:.1f},{ys[i-1]:.1f} {cx:.1f},{ys[i]:.1f} {xs[i]:.1f},{ys[i]:.1f}'
    return d
def walk(n, start, vol, lo, hi, drift=0):
    v=start; out=[]
    for i in range(n):
        v += random.gauss(drift, vol); v=max(lo,min(hi,v)); out.append(v)
    return out
def linechart(series, w=860, h=170, lo=0, hi=1, yl=None, xl=None, fill=False, inv=False):
    s=f'<svg width="{w+40}" height="{h+30}" viewBox="-36 -6 {w+40} {h+30}" style="display:block">'
    for k in range(5):
        y=h*k/4; s+=f'<line x1="0" x2="{w}" y1="{y}" y2="{y}" stroke="#252A2E"/>'
        if yl: s+=f'<text x="-8" y="{y+3}" fill="#81878D" font-size="10" text-anchor="end">{yl[k]}</text>'
    if xl:
        for k,t in enumerate(xl):
            an='start' if k==0 else 'end' if k==len(xl)-1 else 'middle'
            s+=f'<text x="{k*w/(len(xl)-1)}" y="{h+18}" fill="#81878D" font-size="10" text-anchor="{an}">{t}</text>'
    for pts,col in series:
        lo2,hi2=(hi,lo) if inv else (lo,hi)
        d=path(pts,w,h,lo2,hi2)
        if fill: s+=f'<path d="{d} L{w},{h} L0,{h}Z" fill="{col}" opacity=".12"/>'
        s+=f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2"/>'
    return s+'</svg>'
