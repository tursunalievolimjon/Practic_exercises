# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
from datetime import datetime
bugun = datetime.now()
data = int(bugun.strftime('%Y'))
yosh = int(input('Yoshingiz nechida?\n>>>>'))
print('Siz',data-yosh,'yilda tug\'ilgansiz')