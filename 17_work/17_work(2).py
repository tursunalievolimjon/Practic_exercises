### \\\ 2_work

chipta = 'Yoshingizni kiriting'
chipta += ' (dasturni toxtatishni hohlasangiz "exit" yoki "quit" deb yozing):'
while True:
    yosh = input(chipta)
    if yosh == 'exit' or yosh == 'quit':
        break
    yosh = float(yosh)
    if yosh <= 7:
        print(f'Chipta narhi 2000 so\'m')
    elif 7 < yosh <= 18:
        print(f'Chipta narhi 3000 so\'m')
    elif 18 < yosh <= 65:
        print(f'Chipta narhi 10000 so\'m')
    else:
        print(f'Chipta narhi tekin')
print('Dastur tugadi')