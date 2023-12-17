def ism_va_yosh_chiqar(ism,yosh):
    '''Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya'''
    print(f'Sizning ismingiz {ism.title()} va {2023 - int(yosh)}-yilda tug\'ilgan siz')
ism_va_yosh_chiqar(ism=input('Ismingiz nima:'),yosh=input('Yoshingiz nechida:'))