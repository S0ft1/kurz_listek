# kurz_listek
Prerekvizity:

Mít pip a python3

Instalace:

pip install scrapy scrapy-playwright

playwright install

Použití:

Spustit přiložený start.bat soubor (ten pouští python script a obstarává mazání starého outputu, protože řešení přes configuraci knihovny se zdálo být výrazně složitější)
Po doběhnutí scriptu se ve stejném adresáři objeví output.json, tady jsou ty data v jsonu.

Zajímavé fily:

\kurz_listek\output.json (výstupní data)
\kurz_listek\kurz_listek\spiders\table_spider.py (tady se děje samotná scrapovací logika)
\kurz_listek\kurz_listek\settings.py (tady se configuruje Scrapy knihovna aby fungovala s playwright) 
