### \\\ 3_work

dav_poy = {'aqsh':'washington d.c',     # dav_poy = davlat_poytaxt
           'o\'zbekiston':'toshkent',
           'qirg\'iziston':'bishkek',
           'qozog\'iston':'olmota',
           'rossiya':'moskva'
           }

search = input('Qanday davlatning poytaxtini bilishni istaysiz:').lower()
if search in dav_poy:
    dav_poy.keys()
    print(f'{search.capitalize()}-ning poytaxti {dav_poy[search].capitalize()} shahri')
else:
    print('Kechirasiz, bizda bu haqida ma\'lumot yoq')