import asyncio, json, sys, os
HERE=os.path.dirname(os.path.abspath(__file__))
HTML=os.path.join(HERE,'html')
from playwright.async_api import async_playwright
from PIL import Image
OUT=os.path.join(HERE,'out')+'/'
async def main(names):
    import os; os.makedirs(OUT,exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':1200,'height':750},device_scale_factor=2)
        info={}
        for n in names:
            await pg.goto(f'file://{HTML}/{n}.html'); await pg.evaluate('Promise.all([...document.fonts].map(f=>f.load()))'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=OUT+n+'.png',full_page=True)
            info[n]=await pg.evaluate('''()=>{const o={h:document.body.scrollHeight};for(const id of ['kpi','add','chips','moves','removed']){const e=document.getElementById(id);if(e)o[id]=Math.round(e.getBoundingClientRect().top+scrollY)}
              const m=[...document.querySelectorAll('#moves .row')].find(r=>!r.classList.contains('mine'));if(m)o.market=Math.round(m.getBoundingClientRect().top+scrollY);return o}''')
            for sel,name in [('#kpi','c-kpi'),('#row','c-row'),('#filter','c-filter'),('#grid','c-grid'),('#modelcards','c-model')]:
                if n in ('overview','card','models') and await pg.query_selector(sel):
                    if name=='c-filter' and n!='overview': continue
                    await (await pg.query_selector(sel)).screenshot(path=OUT+name+'.png')
            if n=='overview':
                rows=await pg.query_selector_all('#moves .row')
                bb1=await rows[0].bounding_box(); bb2=await rows[3].bounding_box()
                await pg.screenshot(path=OUT+'c-moves.png',clip={'x':bb1['x'],'y':bb1['y'],'width':bb1['width'],'height':bb2['y']+bb2['height']-bb1['y']},full_page=True)
            if n=='texts':
                await (await pg.query_selector('#nav')).screenshot(path=OUT+'c-nav.png')
        await b.close()
        print(json.dumps(info))
asyncio.run(main(sys.argv[1:]))
