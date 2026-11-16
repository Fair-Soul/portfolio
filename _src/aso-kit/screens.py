from kit import *
A = {  # name: (dev, icon, grad, store)
 'ProSign PDF Editor':('Nordwind Apps','pen',0,'Google Play'),
 'OfficeDocs — PDF Editor & Tools':('Delta Soft','doc',1,'App Store'),
 'PaperScan PDF Editor':('Orion Mobile','scan',3,'Google Play'),
 'LumoCam Photo Editor':('Riverbend Apps','cam',5,'App Store'),
 'HyperProxy VPN':('Fast Apps Ltd','shield',4,'Google Play'),
 'DocReader':('Polar Code','doc',2,'Google Play'),
 'QuickEdit — PDF Editor & Tools':('Kite Studio','pen',7,'Google Play'),
 'ProDocs':('Atlas Utilities','doc',8,'App Store'),
 'NovaGate VPN':('Mega Tools Inc','shield',6,'Google Play'),
 'SmartDocs PDF Editor':('Brightline Tech','doc',9,'App Store'),
 'VividLab Photo Editor':('Moonrise Dev','cam',0,'App Store'),
 'BoltProxy VPN':('AppLab 77','shield',3,'Google Play'),
 'EasyReader PDF Editor':('Nordwind Apps','doc',4,'App Store'),
 'PixelLab':('Quiet Pixel LLC','grid',5,'Google Play'),
}
def ic(n, cls=''):
    d,k,g,s = A[n]; return icon(k,g,cls)
MY = ['ProSign PDF Editor','OfficeDocs — PDF Editor & Tools']
VIS = {MY[0]:'24%', MY[1]:'20%'}

# ---------- OVERVIEW ----------
def kpis():
    return f'''<div class="kpis" id="kpi">
<div class="card kpi o"><div class="l">Мои приложения в выдаче</div><div class="v">2<small>из 2</small></div><div class="d">все в топ-10 хотя бы по одному ключу</div></div>
<div class="card kpi"><div class="l">Видимость своих</div><div class="v">22,1%</div><div class="d"><span class="up">▲ 3,4 п.п.</span> к прошлой неделе</div></div>
<div class="card kpi"><div class="l">Удалено своих за 7 дней</div><div class="v">0</div><div class="d">рынок: 9 удалений за неделю</div></div>
<div class="card kpi"><div class="l">В зоне риска</div><div class="v">1</div><div class="d"><span class="wa">OfficeDocs</span> · риск удаления 34%</div></div></div>'''
def myrow(n, chips, rid=''):
    d,k,g,s = A[n]
    ch = ''.join(f'<span class="chip">{kw} <span class="flag">{c}</span><span class="pos {cl}">{p}</span><span class="dl {"up" if dl>0 else "dn" if dl<0 else ""}">{("▲"+str(dl)) if dl>0 else ("▼"+str(-dl)) if dl<0 else "·"}</span></span>' for kw,c,p,cl,dl in chips)
    return f'<div class="row" {rid} style="align-items:flex-start;padding:13px 16px">{ic(n)}<div style="flex:none;width:262px"><div class="nm nw">{n}<span class="tag">моё</span></div><div class="sb">{s} · видимость {VIS[n]} · {d}</div></div><div class="chips" style="flex:1;min-width:0">{ch}</div></div>'
def myapps_block():
    r1 = myrow(MY[0],[('pdf scanner','DE',3,'o',2),('sign pdf','US',4,'t',1),('pdf scanner','US',4,'t',-1),('sign pdf','DE',7,'',1),('pdf editor','BR',10,'',0),('pdf scanner','BR',13,'',-6)], 'id="row"')
    r2 = myrow(MY[1],[('pdf editor','US',2,'o',3),('pdf editor','DE',4,'t',1),('pdf scanner','US',5,'t',1),('sign pdf','DE',7,'',-2),('pdf scanner','DE',9,'',2)])
    add = '''<div style="padding:14px 16px;border-bottom:1px solid var(--ln);display:grid;grid-template-columns:1fr 1fr 150px auto;gap:12px;align-items:end">
<div><div class="sb" style="margin-bottom:5px">Найти среди отслеживаемых</div><div class="sel" style="color:var(--mu)">Название, разработчик или ID</div></div>
<div><div class="sb" style="margin-bottom:5px">Или добавить по ссылке</div><div class="sel" style="color:var(--mu)">Ссылка на App Store или Google Play</div></div>
<div><div class="sb" style="margin-bottom:5px">Страна</div><div class="sel">США (US) ▾</div></div><div class="btn p">Добавить как моё</div></div>'''
    return f'<div class="sec" id="add"><div class="st"><h2>Мои приложения</h2><a>все мои · + добавить своё</a></div><div class="card">{add}<div id="chips">{r1}{r2}</div></div></div>'
MOVES = [
 (MY[1],'вошло в топ-10 по «pdf editor» · App Store · DE',12,4,1),
 (MY[0],'выпало из топ-10 по «pdf editor» · Google Play · BR',7,13,1),
 (MY[0],'поднялось по «pdf scanner» · Google Play · DE',5,3,1),
 (MY[1],'поднялось по «pdf editor» · App Store · US',5,2,1),
 (MY[1],'поднялось по «pdf scanner» · App Store · US',6,5,1),
 (MY[0],'опустилось по «pdf scanner» · Google Play · US',3,4,1),
 ('PaperScan PDF Editor','вошло в топ-10 по «pdf scanner» · Google Play · BR',22,3,0),
 ('LumoCam Photo Editor','вошло в топ-10 по «photo editor» · App Store · US',14,6,0),
 ('HyperProxy VPN','вошло в топ-10 по «vpn» · Google Play · DE',11,6,0),
 ('HyperProxy VPN','вошло в топ-10 по «vpn proxy» · Google Play · BR',15,8,0),
 ('DocReader','выпало из топ-10 по «pdf editor» · Google Play · DE',8,15,0),
 ('QuickEdit — PDF Editor & Tools','вошло в топ-10 по «pdf scanner» · Google Play · US',11,6,0),
 ('ProDocs','вошло в топ-10 по «pdf editor» · App Store · US',12,7,0),
 ('SmartDocs PDF Editor','выпало из топ-10 по «sign pdf» · App Store · DE',9,17,0),
 ('NovaGate VPN','вошло в топ-10 по «vpn» · Google Play · BR',18,9,0),
 ('EasyReader PDF Editor','поднялось по «pdf editor» · App Store · DE',9,6,0),
]
def mvrow(n,t,a,b,mine,when='сегодня в 11:00'):
    cl = 'pos o' if b>10 and mine else ('pos t' if b<=10 else 'pos')
    tag = '<span class="tag">моё</span>' if mine else ''
    return f'<div class="row{" mine" if mine else ""}">{ic(n,"sm")}<div><div class="nm" style="font-size:12px">{n}{tag}</div><div class="sb">{t}</div></div><div class="mv"><span class="pos">{a}</span>→<span class="{cl}">{b}</span><span class="when">{when}</span></div></div>'
def moves(k=16, rid='id="moves"'):
    rows=''.join(mvrow(*m) for m in MOVES[:k])
    return f'<div class="sec" {rid}><div class="st"><h2>Движения в выдаче</h2><a>с прошлой проверки · 35 выдач во всех странах · все движения</a></div><div class="card">{rows}<div class="row"><span class="btn">Показать ещё 16</span></div></div></div>'
def builds():
    B=[('PaperScan PDF Editor','новая сборка 1.1.0 → 1.2.0','12 ч назад'),('HyperProxy VPN','новая сборка 1.2.0 → 1.3.0','12 ч назад'),('VividLab Photo Editor','новая сборка 1.29.0 → 1.30.0','12 ч назад'),('BoltProxy VPN','новая сборка 1.1.0 → 1.2.0','12 ч назад'),('PixelLab','новая сборка 1.2.0 → 1.3.0','12 ч назад'),('SmartDocs PDF Editor','сменил листинг в выдаче по «pdf scanner» · BR: название, иконка','2 дня назад'),('NovaGate VPN','сменил листинг в выдаче по «vpn» · BR: название, иконка','2 дня назад')]
    rows=''.join(f'<div class="row">{ic(n,"sm")}<div class="nm" style="font-size:12px">{n} <span class="sb" style="font-weight:400">· {t}</span></div><span class="mv">{w}</span></div>' for n,t,w in B)
    return f'<div class="sec"><div class="st"><h2>Новые сборки и смена графики</h2><a>вся история в ленте</a></div><div class="card">{rows}</div></div>'
REM=[('EasyPDF','Sato Mobile','doc',2,46,'3 дня назад'),('TurboGuard: Super VPN','Best Free Apps','shield',4,24,'3 дня назад'),('Zen Unlimited VPN Pro','AppLab 77','shield',6,23,'4 дня назад'),('ShieldWall: Super VPN','AppLab 77','shield',8,20,'5 дней назад'),('PageEdit','Atlas Utilities','doc',9,'3 мес','7 дней назад'),('VividArt: Super Photo Editor','Fast Apps Ltd','cam',1,22,'7 дней назад')]
def removed(rid='id="removed"'):
    rows=''.join(f'<div class="row">{icon(k,g,"sm")}<div><div class="nm" style="font-size:12px">{n}</div><div class="sb">{d} · прожило {l}{" дней" if isinstance(l,int) else ""}</div></div><span class="mv">{w}</span></div>' for n,d,k,g,l,w in REM)
    return f'<div class="card">{rows}</div>'
RISK=[('Shield Unlimited VPN Pro','Top Utility Dev','shield',2,100),('Hyper Unlimited VPN Pro','Fast Apps Ltd','shield',5,100),('Paper Unlimited PDF Editor Pro','AppLab 77','doc',3,100),('LumoStudio: Super Photo Editor','Top Utility Dev','cam',1,87),('OfficeDocs — PDF Editor & Tools','Delta Soft','doc',1,34),('FramePic Photo Editor','Brightline Tech','cam',6,15)]
def risk():
    rows=''.join(f'<div class="row{" mine" if "OfficeDocs" in n else ""}">{icon(k,g,"sm")}<div><div class="nm" style="font-size:12px">{n}{"<span class=tag>моё</span>" if "OfficeDocs" in n else ""}</div><div class="sb">{d}</div></div><span class="mv"><b style="color:var(--ink)">{p}%</b><span class="bar"><i style="width:{p}%;background:{"var(--bad)" if p>50 else "var(--wa)"}"></i></span></span></div>' for n,d,k,g,p in RISK)
    return f'<div class="card">{rows}</div>'
def overview():
    b = f'<div class="hd"><h1>Сводка</h1><span class="meta">что изменилось с прошлой проверки · проверено 12 ч назад</span></div>{filt()}{kpis()}{myapps_block()}{moves()}{builds()}'
    b += f'<div class="sec g2"><div><div class="st"><h2>Удалены из стора</h2><a>за 30 дней</a></div>{removed()}</div><div><div class="st"><h2>В зоне риска</h2><a>как считается</a></div>{risk()}</div></div>'
    return page('Сводка', b)

# ---------- POSITIONS ----------
RES=[('LensStudio Photo Editor','Polar Code','cam',5,'4.8',129317),('SnapStudio Photo Editor','Atlas Utilities','cam',6,'4.4',59257),('LensFx Photo Editor','Moonrise Dev','cam',2,'4.7',89887),('ColorPic Photo Editor','Blue Harbor Labs','grid',3,'4.6',29039),('VividLab Photo Editor','Moonrise Dev','cam',0,'4.4',16953),('LumoPic Photo Editor','Riverbend Apps','cam',4,'4.7',43426),('VividCam Photo Editor','Moonrise Dev','cam',8,'4.5',49452),('ColorLab — Photo Editor & Tools','Polar Code','grid',9,'4.6',71937)]
def positions():
    kws=['collage maker','pdf editor','pdf scanner','photo editor','sign pdf','vpn','vpn proxy']
    kl=''.join(f'<div style="padding:9px 11px;border-radius:8px;{"background:var(--s2);" if i==0 else ""}"><div style="font-size:12px;font-weight:600">{k}</div><div class="sb" style="font-size:10px">iOS: US · DE · GP: BR · US · DE</div></div>' for i,k in enumerate(kws))
    rows=''
    for i,(n,d,k,g,r,c) in enumerate(RES):
        dl=random.choice([1,2,-1,0,3,-2])
        rows+=f'''<div class="row" style="padding:12px 16px;gap:14px"><span class="pos t" style="width:30px;height:30px;line-height:30px;font-size:13px;border-radius:8px">{i+1}</span>{icon(k,g)}<div style="width:230px"><div class="nm">{n}</div><div class="sb">{d}</div><div class="sb nw">★ {r} · {f"{c:,}".replace(",", " ")} оценок</div><div class="sb nw">вышло {random.choice(["2 года","8 месяцев","24 месяца","12 месяцев"])} назад</div><div class="sb">прогноз через 7 дн: <span class="{"up" if dl>=0 else "dn"}">{max(1,i+1-dl)}</span></div></div><div style="display:flex;gap:7px;margin-left:auto">{"".join(shot(g+j,j) for j in range(5))}</div></div>'''
    b=f'''<div style="display:grid;grid-template-columns:200px 1fr;gap:18px"><div><div class="card" style="padding:8px"><div style="display:flex;gap:6px;margin-bottom:8px"><div class="sel" style="flex:1;color:var(--mu)">Найти ключ</div><div class="btn">+</div></div>{kl}</div></div>
<div><div class="hd" style="margin-bottom:8px"><h1 style="font-size:24px;text-transform:none">«collage maker»</h1><span class="btn">Изменить ключ</span></div><div class="meta" style="margin-bottom:12px">App Store · US · язык en · проверено 12 ч назад · 34 приложения</div>
<div class="fb"><div class="seg"><span>DE</span><span class="on">US</span></div><div class="seg"><span>BR/en</span><span>DE/en</span><span>US</span></div></div>
<div class="g3" style="grid-template-columns:repeat(5,1fr);margin-bottom:14px">{"".join(f'<div class="card pad" style="padding:12px"><div style="font:800 20px/1 H">{v}</div><div class="sb" style="margin-top:6px">{t}</div></div>' for v,t in [('27','оценка ключа из 100'),('79%','сложность: сила лидеров'),('10%','ротация топ-10 за неделю'),('0%','молодых в топ-10'),('0%','ключ в названии у топ-10')])}</div>
<div class="tabs" style="margin-top:0"><span class="on">Выдача</span><span>История позиций</span></div><div class="card">{rows}</div></div></div>'''
    return page('Позиции и выдача', b)

# ---------- APP CARD (positions) ----------
def apphead(n='ProSign PDF Editor', dev='Nordwind Apps', mine=True, k='pen', g=0, stats=None, tab=0, rel='22.12.2024', base='15.06.2026'):
    stats = stats or [('3','лучшее место сейчас · «pdf scanner» · DE'),('24%','видимость: 1-е место = 100%'),('23 месяца','возраст с выхода в стор'),('меньше 1%','риск удаления за 30 дней')]
    st=''.join(f'<div style="padding:14px 16px;{"border-left:1px solid var(--ln);" if i else ""}"><div style="font:800 22px/1 H">{v}</div><div class="sb" style="margin-top:6px">{t}</div></div>' for i,(v,t) in enumerate(stats))
    tabs=''.join(f'<span class="{"on" if i==tab else ""}">{t}</span>' for i,t in enumerate(['Позиции','Метаданные и графика','История']))
    return f'''<div class="sb" style="margin-bottom:12px">← Приложения</div><div style="display:flex;gap:16px;align-items:center">{icon(k,g,"lg")}<div><div style="font:800 24px/1.1 H">{n}</div><div class="sb" style="margin:4px 0 9px">{dev} · Google Play · US · <span class="up">● в сторе</span> · вышло {rel} · в базе с {base}</div>
<div style="display:flex;gap:8px">{"<span class='btn p'>Моё приложение ✓</span>" if mine else "<span class='btn'>Это моё приложение</span>"}<span class="btn">☆ В избранное</span><span class="btn">Открыть в сторе</span><span class="btn">Ещё ▾</span></div></div></div>
<div class="card" style="display:grid;grid-template-columns:repeat(4,1fr);margin-top:18px">{st}</div><div class="tabs">{tabs}</div>'''
def grid():
    K=[('pdf scanner',[(7,1,6),(3,2,2),(4,-1,3)]),('sign pdf',[(7,1,6),(4,0,3),(3,1,2)]),('pdf editor',[(13,-6,11),(10,0,9),(5,1,4)])]
    h='<table class="tbl" style="font-size:12px"><tr><th>Ключ</th><th class="r">BR</th><th class="r">DE</th><th class="r">US</th></tr>'
    for k,cs in K:
        h+=f'<tr><td style="font-weight:600">{k}</td>'+''.join(f'<td class="r"><span class="pos {"o" if p<=3 else "t" if p<=10 else ""}" style="display:inline-block;min-width:26px;height:24px;line-height:24px;font-size:12px">{p}</span> <span class="dl {"up" if d>0 else "dn" if d<0 else ""}">{"▲"+str(d) if d>0 else "▼"+str(-d) if d<0 else "·"}</span><div class="sb" style="font-size:10px;margin-top:3px">через 7 дн: ~{f}</div></td>' for p,d,f in cs)+'</tr>'
    return f'<div class="card" id="grid" style="max-width:640px">{h}</table></div>'
def card():
    random.seed(3)
    cols=['#FF4D29','#8E9BFF','#49E2A0','#E9BF42']
    ser=[(walk(60,s,.6,1,12),c) for s,c in zip([4,7,3,9],cols)]
    vis=[(walk(60,s,3,5,60,0),c) for s,c in zip([20,30,14],['#FF4D29','#8E9BFF','#49E2A0'])]
    leg=lambda L:'<div style="display:flex;gap:14px;margin-bottom:8px">'+''.join(f'<span class="sb"><i style="display:inline-block;width:8px;height:8px;border-radius:2px;background:{c};margin-right:5px"></i>{t}</span>' for t,c in L)+'</div>'
    xl=['15 июн','1 июл','15 июл','1 авг','15 авг','1 сен','15 сен','1 окт','15 окт','1 ноя']
    b=apphead()+f'''<div class="st"><h2>Позиции по ключам</h2><a>место сейчас и изменение с прошлой проверки</a></div>{grid()}
<div class="sec"><div class="st"><h2>История позиций</h2><a>первое место наверху</a></div><div class="card pad">{leg(list(zip(['pdf scanner · DE','sign pdf · US','pdf scanner · US','sign pdf · DE'],cols)))}{linechart(ser,880,190,1,12,['1','4','7','10','12'],xl,inv=True)}</div></div>
<div class="sec"><div class="st"><h2>Видимость по дням</h2><a>% от первого места: 1-е = 100%</a></div><div class="card pad">{leg(list(zip(['BR','DE','US'],['#FF4D29','#8E9BFF','#49E2A0'])))}{linechart(vis,880,160,0,60,['60%','45%','30%','15%','0%'],xl,fill=True)}</div></div>
<div class="sec"><div class="st"><h2>Чем отличаются лидеры выдачи</h2><a>сравнение с топ-10 по каждому ключу</a></div><div class="card">{"".join(f'<div class="row"><span class="chip">{k}</span><span style="font-size:12px">Лидеры по «{k}» выпускали около {n} обновлений за 90 дней, вы — 4.</span></div>' for k,n in [('pdf editor',9),('pdf scanner',9),('sign pdf',7)])}</div></div>'''
    return page('Все приложения', b)

# ---------- META ----------
def meta():
    shots=''.join(shot(i,i%3) for i in range(7))
    lst=''.join(f'<div class="row" style="padding:12px 16px"><div style="width:250px"><div style="font-size:12px;font-weight:600">«{k}» <span class="flag">{c}</span> <span class="sb">листинг под страну</span></div><div style="display:flex;gap:9px;align-items:center;margin-top:8px">{icon("cam",5,"sm")}<span class="nm">RetroLab {c}</span></div><div class="sb" style="margin-top:6px">отличается: название, иконка · с 21.10.2026</div></div><div style="display:flex;gap:6px;margin-left:auto">{"".join(shot(5+j,j) for j in range(7))}</div></div>' for k,c in [('collage maker','BR'),('photo editor','BR'),('collage maker','DE'),('photo editor','DE')])
    info=''.join(f'<div style="padding:7px 0;border-top:1px solid var(--ln)"><div class="sb" style="font-size:10.5px">{a}</div><div style="font-size:12px">{v}</div></div>' for a,v in [('Категория','Photography'),('Цена','Бесплатно'),('Встроенные покупки','да, $0.99 — $49.99'),('Установки','100 000+'),('Рейтинг','4,43 из 5 · 7 267 оценок'),('Версия','1.3.0'),('Последнее обновление','04.11.2026'),('Вышло в стор','22.06.2026'),('Bundle ID','com.retrolab.app')])
    b=apphead('RetroLab','Moonrise Dev',False,'cam',5,[('6','лучшее место · «collage maker» · BR'),('9%','видимость'),('5 месяцев','возраст с выхода в стор'),('меньше 1%','риск удаления за 30 дней')],1,rel='22.06.2026',base='23.06.2026')
    b+=f'''<div class="st"><h2>Устройства и графика</h2><a>Google Play не сообщает список устройств</a></div><div class="card pad" style="display:flex;gap:8px;align-items:center"><div style="width:110px"><div class="nm">Android</div><div class="sb">7 скриншотов и видео</div></div>{shots}</div>
<div class="sec"><div class="st"><h2>Листинги в выдаче</h2><a>картинка в выдаче по ключу, если отличается от страницы</a></div><div class="card">{lst}</div></div>
<div class="sec" style="display:grid;grid-template-columns:1.5fr 1fr;gap:14px"><div><div class="st"><h2>Описание</h2><a>590 символов</a></div><div class="card pad"><div class="nm" style="margin-bottom:8px">Удобный photo editor в один клик</div><div class="sb" style="font-size:12px;line-height:1.6;color:#b9c0c6">RetroLab — фоторедактор с плёночными фильтрами, коллажами и ретушью. Соберите коллаж из 9 фото, добавьте рамку и текст, сохраните в высоком качестве. Подходит для сторис, постов и печати.</div><div class="nm" style="margin:14px 0 6px">Что нового в 1.3.0</div><div class="sb">Новые рамки для коллажей, ускорен экспорт.</div></div></div><div><div class="st"><h2>Сведения</h2><a>на 13.11.2026</a></div><div class="card" style="padding:4px 16px">{info}</div></div></div>'''
    return page('Все приложения', b)

# ---------- HISTORY ----------
def history():
    stg=''.join(f'<div class="card" style="padding:11px 12px"><div class="sb" style="font-size:10px">{d}</div><div style="font-size:12px;margin-top:4px">{t}</div></div>' for d,t in [('22.06.2026','Вышло в стор'),('23.06.2026','Попало в базу по «photo editor», 14-е место'),('13.07.2026','Первый отдельный листинг в выдаче'),('21.09.2026','Впервые в топ-10: 10-е место'),('05.11.2026','Лучшее место: 6-е по «collage maker» · BR')])
    EV=[('05.11.2026 · 11:00','Обновление 1.2.0 → 1.3.0','Новые рамки для коллажей, ускорен экспорт.',1),('21.10.2026 · 11:00','Сменился листинг в выдаче по «collage maker» · BR: название, иконка','',0),('21.10.2026 · 11:00','Сменился листинг в выдаче по «photo editor» · DE: название, иконка','',0),('11.10.2026 · 11:00','Изменилось описание','Добавлены «коллаж» и «ретро» в первые строки.',0),('04.10.2026 · 11:00','Установки: 10 000+ → 100 000+','',0),('21.09.2026 · 11:00','Обновление 1.1.0 → 1.2.0','Исправления ошибок.',1),('06.09.2026 · 11:00','По «collage maker» · BR снова показывается основная страница','',0),('13.07.2026 · 11:00','Другой листинг в выдаче по «photo editor» · BR','',0),('07.07.2026 · 11:00','Установки: 1 000+ → 10 000+','',0),('01.07.2026 · 11:00','Обновление 1.0.0 → 1.1.0','Исправления ошибок.',1),('23.06.2026 · 11:00','Найдено по ключу «photo editor», место 14','',0),('22.06.2026','Вышло в стор','',1)]
    ev=''.join(f'<div style="display:flex;gap:12px;padding:0 0 14px;position:relative"><div style="width:9px;height:9px;border-radius:50%;margin-top:4px;flex:none;background:{"var(--ac)" if big else "#3a4045"}"></div><div><div class="sb" style="font-size:10.5px">{d}</div><div style="font-size:12.5px;{"font-weight:600" if big else ""}">{t}</div>{f"<div class=sb style=margin-top:5px;background:var(--s2);padding:6px 9px;border-radius:6px>{x}</div>" if x else ""}</div></div>' for d,t,x,big in EV)
    random.seed(9); r=[1000+i*i*1.25+random.random()*80 for i in range(70)]
    oth=''.join(f'<div class="row">{icon(k,g,"sm")}<span class="nm" style="font-size:12px">{n}</span><span class="mv"><span class="{"dn" if rm else "up"}">● {"удалено 11.07" if rm else "в сторе"}</span></span></div>' for n,k,g,rm in [('TurboWall VPN','shield',6,0),('ShieldProxy VPN','shield',4,0),('SwiftTunnel VPN','shield',8,0),('AstraGuard VPN','shield',0,0),('QuickScan PDF Editor','scan',2,1),('RetroFx Photo Editor','cam',3,0)])
    b=apphead('RetroLab','Moonrise Dev',False,'cam',5,[('6','лучшее место · «collage maker» · BR'),('9%','видимость'),('5 месяцев','возраст с выхода в стор'),('меньше 1%','риск удаления за 30 дней')],2,rel='22.06.2026',base='23.06.2026')
    b+=f'''<div class="st"><h2>Этапы</h2><a>путь приложения: от выхода до сегодня</a></div><div style="display:grid;grid-template-columns:repeat(5,1fr);gap:10px">{stg}</div>
<div class="sec" style="display:grid;grid-template-columns:1.25fr 1fr;gap:18px"><div><div class="st"><h2>События</h2><a>4 версии · 3 смены метаданных</a></div><div class="card pad" style="padding:16px 16px 4px">{ev}</div></div>
<div><div class="st"><h2>Число оценок</h2><a>рост аудитории</a></div><div class="card pad">{linechart([(r,"#FF4D29")],380,150,0,8000,["8k","6k","4k","2k","0"],["июл","авг","сен","окт","ноя"],fill=True)}</div>
<div class="st" style="margin-top:18px"><h2>Другие приложения разработчика</h2><a>7 в базе</a></div><div class="card">{oth}</div></div></div>'''
    return page('Все приложения', b)
