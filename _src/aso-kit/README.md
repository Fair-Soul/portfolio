# AezakmiSO demo-screen kit

Generates the AezakmiSO case screens (demo data, invented app names) as HTML in the tool's design system, then renders them at 2x.

    python3 screens2.py                 # writes html/*.html
    python3 render.py overview card ... # writes out/*.png (needs playwright + Chrome)

Then convert out/*.png to WebP into ../../img/aso/. Overview tour stops (data-y in index.html) come from the offsets render.py prints.
Files: kit.py (CSS, icons, sidebar, charts), screens.py (overview, positions, card, meta, history), screens2.py (niche, models, texts, myapps, login).
