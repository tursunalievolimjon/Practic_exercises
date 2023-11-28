### \\\ 2_work

dav_poy = {'aqsh':'washington d.c',     # dav_poy = davlat_poytaxt
           'o\'zbekiston':'toshkent',
           'qirg\'iziston':'bishkek',
           'qozog\'iston':'olmota',
           'rossiya':'moskva'
           }

print('Davlatlar:')
for dav in sorted(dav_poy):
    print(dav.title())
print('\nPoytaxtlar:')
for poy in sorted(dav_poy.values()):
    print(poy.title())