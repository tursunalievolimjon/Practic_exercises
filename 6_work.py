# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
son = int(input('Istalgan son kiriting:\n>>>>'))
print(son,'ning kvadrati',son**2,'ga teng')
print(son,'ning kubi',son**3,'ga teng')

# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
from datetime import datetime
bugun = datetime.now()
data = int(bugun.strftime('%Y'))
yosh = int(input('Yoshingiz nechida?\n>>>>'))
print('Siz',data-yosh,'yilda tug\'ilgansiz')

# Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
a = float(input('Birinchi sonni kiriting:'))
b = float(input('\nIkkinchi sonni kiriting:'))
print(a,'+',b,'=',a+b)
print(a,'-',b,'=',a-b)
print(a,'*',b,'=',a*b)
print(a,'/',b,'=',a/b)
input()
