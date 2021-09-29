# ExcelDataEntry
Program ktorý zobrazí okno - formulár na vkladanie údajov do Excel tabuľky

Podľa návodu: https://www.youtube.com/watch?v=svcv8uub0D0


Aby program fungoval aj u niekoho kto nemá Python, treba mu spolu so súborom table_entry.py poslať aj inštalačný súbor, ktorý sa vytvorí cez Terminál takto:

>pip install pyinstaller

>pyinstaller --onefile --noconsole table_entry.py

V projekte sa vytvorí o.i. zložka dist z ktorej treba presunúť súbor table_entry.exe(alebo table_entry.app) do spoločnej zložky projektu k súboru table_entry.py

Novovytvorené zložky dist, build a _pycache_ potom možeme zmazať, už nám ich netreba. Na spustenie formulára stačí spustiť table_entry.app

