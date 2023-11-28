### \\\ 1_work

py_lugat = {'float':'o\'nlik son',
            'int':'butun son',
            'string':'matn',
            'tuple':'o\'zgarmas ro\'yhat',
            'list':'ro\'yhat',
            'dict':'lug\'at',
            'while':'tuganmas tsikl',
            'for':'qaytariluvchi tsikl'
            }
for k,q in py_lugat.items():    # k = kalit, q = qiymat
    print(f'{k.capitalize()} - {q.capitalize()}')