davlatlar = {'o\'zbekiston':{'poy':'toshkent',
                             'maydon':448900,
                             'aholi':36024946,
                             'pul_birligi':'so\'m'},
             'turkiya':{'poy':'ankara',
                        'maydon':783562,
                        'aholi':84780000,
                        'pul_birligi':'lira'},
             'saudiya arabiya':{'poy':'Er-riyyad',
                        'maydon':2150000,
                        'aholi':37852658,
                        'pul_birligi':'rial'},
             'buyuk britaniya':{'poy':'london',
                        'maydon':243610,
                        'aholi':69425995,
                        'pul_birligi':'funt-sterling'}}
#
for d_nomi,info in davlatlar.items():
    print(f'{d_nomi.capitalize()}-ning poytaxti {info['poy'].title()}')
    print(f'Maydoni {info['maydon']} kv.km'
          f'\nAholisi {info['aholi']}-ta'
          f'\nPul_birligi - {info['pul_birligi']}')