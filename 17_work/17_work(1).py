### \\\ 1_work

kitob = 'Yahshi ko\'rgan kitobingizni kiriting'
kitob += ' (dasturni toxtatishni hohlasangiz "stop" deb yozing):'
while kitob != 'stop':
    qiymat = input(kitob)
    if qiymat != 'stop':
        print(qiymat.title())
    else:
        break
print('Dastur toxtadi')