### \\\ 3_work(a)

py_lugat = {'integer':'Butun son',
        'float':'O\'nlik son',
        'list':'Ro\'yhat',
        'tuple':'O\'zgarmas ro\'yhat',
        'string':'Matn',
        'while':'tsikl',
        'if':'funktsiya'            
        }
soz = input('Kalit so\'z kiriting: ')
print(py_lugat.get(soz,'Bunday so\'z mavjud emas'))