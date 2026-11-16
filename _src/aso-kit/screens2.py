from screens import *

def bars(vals, labels, w=380, h=150, col='#E26C82', hl=None):
    n=len(vals); bw=w/n*.62; m=max(vals)
    s=f'<svg width="{w+30}" height="{h+34}" viewBox="-26 -4 {w+30} {h+34}" style="display:block">'
    for k in range(5):
        y=h*k/4; s+=f'<line x1="0" x2="{w}" y1="{y}" y2="{y}" stroke="#252A2E"/><text x="-7" y="{y+3}" fill="#81878D" font-size="10" text-anchor="end">{round(m*(4-k)/4)}</text>'
    for i,v in enumerate(vals):
        x=i*w/n+(w/n-bw)/2; bh=v/m*h
        s+=f'<rect x="{x:.1f}" y="{h-bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="3" fill="{col}" opacity="{1 if i==hl or hl is None else .45}"/><text x="{x+bw/2:.1f}" y="{h+16}" fill="#81878D" font-size="9.5" text-anchor="middle">{labels[i]}</text>'
    return s+'</svg>'
def hbars(items, w=520):
    m=max(v for _,v in items); s=''
    for t,v in items:
        s+=f'<div style="display:grid;grid-template-columns:190px 1fr 50px;gap:10px;align-items:center;padding:4px 0"><span class="sb" style="text-align:right">{t}</span><span style="height:9px;border-radius:3px;background:var(--ac);width:{v/m*100:.0f}%"></span><span class="sb" style="font-size:11px">{v}</span></div>'
    return s

def niche():
    random.seed(4)
    surv=[100*math.exp(-i/14)*.62+38-i*.004 if i<200 else 0 for i in range(0,120)]
    surv=[max(0,100 if i==0 else 38+62*math.exp(-i/11)-i*.03) for i in range(120)]
    sv=f'<svg width="410" height="190" viewBox="-30 -6 410 190" style="display:block">'
    for k in range(5):
        y=160*k/4; sv+=f'<line x1="0" x2="370" y1="{y}" y2="{y}" stroke="#252A2E"/><text x="-7" y="{y+3}" fill="#81878D" font-size="10" text-anchor="end">{100-25*k}%</text>'
    pts=' '.join(f'{i*370/119:.1f},{160-v*1.6:.1f}' for i,v in enumerate(surv))
    sv+=f'<polygon points="0,160 {pts} 370,160" fill="#FF4D29" opacity=".12"/><polyline points="{pts}" fill="none" stroke="#FF4D29" stroke-width="2"/>'
    x62=62*370/119; sv+=f'<line x1="{x62}" x2="{x62}" y1="0" y2="160" stroke="#E8EDF1" stroke-dasharray="3 3" opacity=".6"/><text x="{x62+5}" y="12" fill="#E8EDF1" font-size="10">медиана 62 дня</text>'
    for k,t in enumerate(['0','200','400','600','800','1000']): sv+=f'<text x="{k*74}" y="176" fill="#81878D" font-size="10" text-anchor="middle">{t}</text>'
    sv+='</svg>'
    hist=bars([5,14,31,48,17,9,4,2],['до 7','8–14','15–30','31–60','61–90','91–180','181–365','>1 г'],380,150,'#E26C82',3)
    rem=''.join(f'<tr><td><div style="display:flex;gap:9px;align-items:center">{icon(k,g,"sm")}<div><div class="nm" style="font-size:12px">{n}</div><div class="sb">{d} · {s}</div></div></div></td><td>{dt}</td><td class="r"><b>{l}</b></td><td class="r">{u}</td><td class="r">{o}</td></tr>' for n,d,k,g,s,dt,l,u,o in [
     ('EasyPDF','Sato Mobile','doc',2,'Google Play · US','11.11.2026','48 дней','5 дней','2 539'),('TurboGuard: Super VPN','Best Free Apps','shield',4,'Google Play · US','10.11.2026','24 дня','24 дня','212'),('Zen Unlimited VPN Pro','AppLab 77','shield',6,'App Store · US','09.11.2026','23 дня','23 дня','526'),('ShieldWall: Super VPN','AppLab 77','shield',8,'Google Play · US','08.11.2026','20 дней','20 дней','380'),('Lumo Unlimited Photo Editor Pro','Fast Apps Ltd','cam',1,'App Store · US','07.11.2026','26 дней','26 дней','654'),('PageEdit','Atlas Utilities','doc',9,'Google Play · DE','06.11.2026','3 месяца','33 дня','2 874'),('BoltGuard: Super VPN','AppLab 77','shield',3,'App Store · US','05.11.2026','12 дней','12 дней','278')])
    dev=''.join(f'<tr><td>{n} <span class="sb">{s}</span></td><td class="r">{a}</td><td class="r">{r} <span class="bar" style="width:50px"><i style="width:{r/a*100:.0f}%"></i></span></td></tr>' for n,s,a,r in [('Polar Code','App Store',16,3),('Blue Harbor Labs','App Store',13,1),('Nordwind Apps','App Store',12,6),('Brightline Tech','Google Play',12,1),('Sato Mobile','Google Play',11,3),('Mega Tools Inc','Google Play',9,9),('AppLab 77','App Store',9,8),('Top Utility Dev','Google Play',9,8)])
    wk=[(random.randint(6,22),random.randint(1,9)) for _ in range(22)]
    wks='<svg width="410" height="150" viewBox="0 0 410 150" style="display:block">'+''.join(f'<rect x="{i*18.5}" y="{130-a*5}" width="7" height="{a*5}" rx="2" fill="#E8EDF1" opacity=".7"/><rect x="{i*18.5+8}" y="{130-r*5}" width="7" height="{r*5}" rx="2" fill="#E26C82"/>' for i,(a,r) in enumerate(wk))+'<line x1="0" x2="410" y1="130.5" y2="130.5" stroke="#252A2E"/></svg>'
    b=f'''<div class="hd"><h1>Ниша и сроки жизни</h1><div class="seg"><span class="on">Сроки жизни</span><span>Выжившие и удалённые</span></div></div>{filt()}
<div id="answer"><div style="font:900 34px/1.08 GH,G;text-transform:uppercase;max-width:760px">Половина приложений исчезает из стора за <span style="color:var(--ac)">62 дня</span></div>
<div class="sb" style="font-size:12.5px;margin:10px 0 16px;max-width:640px">Доля удалённых за 7 дней — 4%, за 30 дней — 40%, за 90 дней — 57%. Оценка учитывает и тех, кто ещё жив, и тех, кого мы нашли уже не новыми.</div>
<div style="display:flex;gap:34px;align-items:center"><div><div style="font:800 26px/1 GH,G">285</div><div class="sb">найдено</div></div><span class="sb" style="font-size:20px">→</span><div><div style="font:800 26px/1 GH,G">108</div><div class="sb">удалено</div></div><div><div style="font:800 26px/1 GH,G">22 дня</div><div class="sb">медиана жизни удалённых</div></div></div></div>
<div class="sec g2"><div><div class="st"><h2>Сколько доживает</h2><a>по возрасту приложения</a></div><div class="card pad">{sv}</div></div><div><div class="st"><h2>Когда удаляют</h2><a>108 удалённых · дней с выхода</a></div><div class="card pad">{hist}</div></div></div>
<div class="sec"><div class="st"><h2>Удалённые из стора</h2><a>сначала недавние · срок жизни всего и после последней сборки</a></div><div class="card"><table class="tbl"><tr><th>Приложение</th><th>Удалено</th><th class="r">Прожило</th><th class="r">После последней сборки</th><th class="r">Оценок</th></tr>{rem}</table></div></div>
<div class="sec g2"><div><div class="st"><h2>Новые и удалённые по неделям</h2><a><span style="color:var(--ink)">■</span> найдено · <span class="dn">■</span> удалено</a></div><div class="card pad">{wks}</div></div><div><div class="st"><h2>Разработчики</h2><a>у кого больше всего приложений</a></div><div class="card"><table class="tbl"><tr><th>Разработчик</th><th class="r">Приложений</th><th class="r">Удалено</th></tr>{dev}</table></div></div></div>'''
    return page('Ниша и сроки жизни', b)

def mcard(t,d,w):
    return f'<div class="card pad"><div style="display:flex;justify-content:space-between;align-items:center"><div style="font:800 12.5px/1 GH,G;text-transform:uppercase">{t}</div><span class="badge ok">работает</span></div><div style="font-size:12px;color:#b9c0c6;margin:10px 0">{d}</div><div class="sb" style="font-size:10.5px;border-top:1px solid var(--ln);padding-top:8px">Где видно: {w}</div></div>'
def models():
    T=[('Модель (градиентный бустинг)','1,92','79,4%','93,5%',1),('Позиция не изменится','2,93','68,2%','88,5%',0),('Средняя позиция за неделю','2,47','70,6%','90,9%',0),('Тренд недели продолжится','4,69','50,5%','81,5%',0)]
    tb=''.join(f'<tr style="{"background:#1d1410" if m else ""}"><td style="{"font-weight:600" if m else ""}">{a}</td><td class="r">{b}</td><td class="r">{c}</td><td class="r">{d}</td></tr>' for a,b,c,d,m in T)
    R=[('Модель (градиентный бустинг)','0,947','0,912',1),('Доля удалённых у разработчика','0,871','0,831',0),('Число изменений метаданных','0,760','0,675',0),('Случайное угадывание','0,500','0,303',0)]
    rb=''.join(f'<tr style="{"background:#1d1410" if m else ""}"><td style="{"font-weight:600" if m else ""}">{a}</td><td class="r">{b}</td><td class="r">{c}</td></tr>' for a,b,c,m in R)
    risk2=''.join(f'<div class="row">{icon(k,g,"sm")}<div><div class="nm" style="font-size:12px">{n}</div><div class="sb">{d}</div></div><span class="mv"><b style="color:var(--ink)">{p}%</b><span class="bar"><i style="width:{p}%;background:{"var(--bad)" if p>50 else "var(--wa)"}"></i></span><span class="when">{dt}</span></span></div>' for n,d,k,g,p,dt in [('LumoStudio: Super Photo Editor','Top Utility Dev','cam',1,100,'28.10.2026'),('Paper Unlimited PDF Editor Pro','AppLab 77','doc',3,100,'26.10.2026'),('NovaGate: Super VPN','Mega Tools Inc','shield',6,100,'19.10.2026'),('PixelFx Photo Editor','Polar Code','cam',8,40,'15.08.2026'),('FramePic Photo Editor','Brightline Tech','cam',5,34,'04.08.2026'),('ZenProxy VPN','Quiet Pixel LLC','shield',2,15,'30.09.2026'),('ClearReader PDF Editor','Moonrise Dev','doc',4,15,'31.10.2026')])
    b=f'''<div class="hd"><h1>Прогнозы и модели</h1><span class="btn">Пересчитать модели</span></div><div class="seg" style="display:inline-flex;margin-bottom:12px"><span class="on">App Store</span><span>Google Play</span></div>
<div class="sb" style="font-size:12.5px;max-width:720px;margin-bottom:16px">Добавлять ничего не нужно: раз в 24 часа модели сами учатся на всех отслеживаемых приложениях. Сейчас это 146 приложений, 14 выдач и история за 151 день. App Store и Google Play учатся отдельно.</div>
<div class="g3" id="modelcards">{mcard("Прогноз позиции","Где окажется приложение по ключу в стране через 7 дней.","колонка «через 7 дн» в выдаче и в карточке")}{mcard("Риск удаления","Вероятность, что живое приложение исчезнет из стора в ближайшие 30 дней.","«В зоне риска» на сводке, карточка")}{mcard("Оценка ключа","0–100: насколько реально подняться в топ-10 по ключу.","шапка выдачи, «Позиции»")}</div>
<div class="sb" style="margin:12px 0 0;max-width:720px">Ниже — как каждая модель проверена: её прогнозы сравниваются с тем, что случилось на самом деле, и с простыми правилами. Если правило не хуже модели — экран говорит об этом.</div>
<div class="sec"><div class="st"><h2>Прогноз позиции через 7 дней</h2><a>обучена 12 ч назад · 22 378 примеров · проверка на 14 756</a></div><div class="card"><table class="tbl"><tr><th>Способ</th><th class="r">Средняя ошибка, мест</th><th class="r">Ошибка не больше 3 мест</th><th class="r">Верно угадан топ-10</th></tr>{tb}</table></div></div>
<div class="sec g2"><div><div class="st"><h2>Что сильнее всего влияет</h2><a>на прогноз позиции</a></div><div class="card pad">{hbars([("Средняя позиция за неделю",6.82),("Дней с последнего обновления",0.76),("Обновлений за месяц",0.34),("Позиция сейчас",0.22),("Разброс позиции за 2 нед.",0.14),("Рейтинг",0.13)])}</div></div>
<div><div class="st"><h2>Риск удаления в ближайшие 30 дней</h2><a>824 примера · проверка на 109</a></div><div class="card"><table class="tbl"><tr><th>Способ</th><th class="r">ROC AUC</th><th class="r">AP</th></tr>{rb}</table></div></div></div>
<div class="sec"><div class="st"><h2>Сейчас в зоне риска</h2><a>живые приложения с самой высокой вероятностью удаления</a></div><div class="card">{risk2}</div></div>'''
    return page('Прогнозы и модели', b)

def texts():
    N=[('Замечания','3 из 5','своих приложений в выдаче, у которых текст мешает хотя бы по одному ключу','wa'),('Оценщик названия','мало смен для проверки','Включится, когда наберётся 5 приложений, у которых оценка после смены выросла, и 5 — у которых упала.','wa'),('Оценщик описания','мало смен для проверки','Пока советы «поменяйте так» не показываются: тексту нечего проверять.','wa')]
    nc=''.join(f'<div class="card pad"><div style="display:flex;justify-content:space-between;align-items:center;gap:8px"><b style="font:800 11.5px/1 GH,G;text-transform:uppercase">{t}</b><span class="badge {c}">{s}</span></div><div class="sb" style="margin-top:9px;font-size:11.5px">{d}</div></div>' for t,s,d,c in N)
    RW=[(MY[0],5,'нет слов ключа: scanner, sign','✕ 4 ключа','без замечаний','dn'),(MY[1],4,'нет слов ключа: sign','✕ 1 ключ','в App Store не влияет на поиск','dn')]
    rows=''.join(f'<tr><td><div style="display:flex;gap:10px;align-items:center">{ic(n,"sm")}<div><div class="nm" style="font-size:12px">{n}<span class="tag">моё</span></div><div class="sb">{A[n][0]}</div></div></div></td><td class="r">{k}</td><td><span class="dn">{x}</span><div class="sb">{t}</div></td><td><span class="up">✓</span> <span class="sb">{o}</span></td></tr>' for n,k,t,x,o,_ in RW)
    det=''.join(f'<tr><td><b>{k}</b> <span class="flag">{c}</span> <span class="sb">{p} место</span></td><td>{n}</td><td>{"<span class=up>✓ все слова ключа в названии</span>" if ok else "<span class=dn>✕ нет слов ключа: "+m+"</span>"}</td></tr>' for k,c,p,n,ok,m in [('pdf scanner','DE',3,'ProSign PDF Editor',0,'scanner'),('sign pdf','US',4,'ProSign PDF Editor',0,'sign'),('pdf scanner','US',4,'ProSign PDF Editor',0,'scanner'),('sign pdf','DE',7,'ProSign PDF Editor',0,'sign'),('pdf editor','BR',10,'ProSign PDF Editor',1,'')])
    b=f'''<div class="hd"><h1>Тексты</h1><span class="meta">что в названиях и описаниях своих приложений мешает по их ключам</span></div><div class="g3">{nc}</div>
<div class="sec"><div class="st"><h2>Тексты своих приложений</h2><a>2 из 2 · по ключам, где приложение сейчас в выдаче</a></div><div class="card"><table class="tbl"><tr><th>Приложение</th><th class="r">Ключей</th><th>Название</th><th>Описание</th></tr>{rows}</table></div></div>
<div class="sec"><div class="st"><h2>ProSign PDF Editor · название по ключам</h2><a>Google Play</a></div><div class="card"><table class="tbl"><tr><th>Ключ</th><th>Название в выдаче</th><th>Что мешает</th></tr>{det}</table></div></div>'''
    return page('Тексты', b)

def myapps():
    rows=''.join(f'<tr><td><span class="pos {"o" if bp<=3 else "t"}" style="display:inline-block">{bp}</span> <span class="dl up">▲{d}</span></td><td><div style="display:flex;gap:10px;align-items:center">{ic(n,"sm")}<div><div class="nm" style="font-size:12px">{n}<span class="tag">моё</span></div><div class="sb">{A[n][0]} · {A[n][3]}</div></div></div></td><td><span class="dn">{kk}</span><div class="sb">{kt}</div></td><td class="r">{r}</td><td class="r">{o}</td><td class="r">{age}</td><td><span class="up">● в сторе</span></td><td class="r">{rk}</td></tr>' for bp,d,n,kk,kt,r,o,age,rk in [(3,2,MY[0],'5 ключей','нет слов ключа: scanner, sign','4,5','99 929','23 месяца','меньше 1%'),(2,3,MY[1],'4 ключа','нет слов ключа: sign','4,3','104 517','23 месяца','34%')])
    vis=[(walk(40,s,1.6,5,40,.05),c) for s,c in [(20,'#FF4D29'),(16,'#8E9BFF')]]
    b=f'''<div class="hd"><h1>Мои приложения</h1><span class="meta">2 приложения · отмечены как свои</span></div>{filt('<div><label>Сортировка</label><div class="sel">По месту в выдаче ▾</div></div>')}
<div class="card"><table class="tbl"><tr><th>Лучшее место</th><th>Приложение</th><th>Название</th><th class="r">Рейтинг</th><th class="r">Оценок</th><th class="r">Возраст</th><th>Статус</th><th class="r">Риск</th></tr>{rows}</table></div>
<div class="sec"><div class="st"><h2>Видимость своих за 40 дней</h2><a><span style="color:#FF4D29">■</span> ProSign · <span style="color:#8E9BFF">■</span> OfficeDocs</a></div><div class="card pad">{linechart(vis,880,130,0,40,["40%","30%","20%","10%","0%"],["6 окт","13 окт","20 окт","27 окт","3 ноя","10 ноя"],fill=True)}</div></div><div class="sec"><div class="st"><h2>ProSign PDF Editor · позиции по ключам</h2><a>место сейчас и прогноз через 7 дней</a></div>{grid()}</div>'''
    return page('Мои приложения', b)

def login():
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
.lg{{display:grid;grid-template-columns:1.6fr 1fr;height:750px}}.l{{background:var(--ac);position:relative;overflow:hidden;padding:48px 40px;color:#140603}}
.l h2{{font:900 64px/.95 GH,G;text-transform:uppercase;margin-top:170px;position:relative;z-index:1}}.l svg{{position:absolute;right:-70px;top:-20px;height:800px;opacity:.95;fill:#140603}}
.f{{padding:0 70px;display:flex;flex-direction:column;justify-content:center}}.in{{height:38px;border:1px solid var(--ln);border-radius:8px;background:var(--s);margin:6px 0 16px}}</style></head><body><div class="lg"><div class="l">
<div style="font:italic 900 26px/1 A">AEZAKMI <span style="background:#140603;color:var(--ac);font:800 11px/1 GH,G;padding:3px 5px;border-radius:3px;vertical-align:4px">SO</span></div><svg viewBox="0 0 100 160"><path d="M62 0 L8 92 H44 L30 160 L92 58 H56 Z"/></svg><h2>Видеть<br>стор<br>раньше</h2><div style="position:absolute;bottom:34px;left:40px;font:600 11px/1 G;letter-spacing:1px">AEZAKMI GROUP · ASO · позиции · удаления · тренды</div></div>
<div class="f"><div style="font:900 24px/1 GH,G;text-transform:uppercase">Вход</div><div class="sb" style="margin:8px 0 22px">Доступ выдаёт администратор команды</div><div class="sb">Логин</div><div class="in"></div><div class="sb">Пароль</div><div class="in"></div><div class="btn p" style="height:40px">Войти</div></div></div></body></html>'''

SCREENS = dict(overview=overview, positions=positions, card=card, meta=meta, history=history, niche=niche, models=models, texts=texts, myapps=myapps, login=login)
if __name__=='__main__':
    os.makedirs(''+os.path.join(os.path.dirname(os.path.abspath(__file__)),'html')+'', exist_ok=True)
    for k,f in SCREENS.items():
        random.seed(sum(map(ord,k)))
        open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'html',k+'.html'),'w').write(f())
    print('ok')
