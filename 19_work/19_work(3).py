def juft_son_faqat(son):
    '''Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya'''
    if son % 2 == 0:
        print(f'{son} juft son hisoblanadi')
    else:
        print(f'{son} toq son hisoblanadi')
juft_son_faqat(son=int(input('Son kiriting:')))