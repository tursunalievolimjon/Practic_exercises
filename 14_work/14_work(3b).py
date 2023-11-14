### \\\ 3_work(b)

py_lugat = {'integer':'Butun son',
        'float':'O\'nlik son',
        'list':'Ro\'yhat',
        'tuple':'O\'zgarmas ro\'yhat',
        'string':'Matn',
        'while':'tsikl',
        'if':'funktsiya'            
        }
soz = input('Kalit so\'z kiriting: ')
if soz not in py_lugat:
    print('Bunday so\'z mavjud emas')
else:
    print(f'{soz.title()} so\'zi {py_lugat[soz]} deb tarjima qilinadi')