# 10_work
# while True:

# \\\ Yangi cars = ['toyota','mazda','hyundai','gm','kia'] degan ro'yhat tuzing,
# ro'yhat elementlarining birinchi harfini katta qilib konsolga chiqaring. GM uchun ikkala harfni katta qiling
# cars = ['toyota','mazda','hyundai','gm','kia']
# for car in cars:
#     if car =='gm':
#         print(car.upper())
#     else:
#         print(car.title())

# \\\ Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring
    # cars = ['toyota','mazda','hyundai','gm','kia']
    # for car in cars:
    #     if car !='gm':
    #         print(car.title())
    #     else:
    #         print(car.upper())

# \\\ Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz,Admin.
# Foydalanuvchilar ro'yhatini  ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"
# matnini konsolga chiqaring
    # foydalanuvchi_ismi = input('login ismingiz nima?\n>>>>')
    # if foydalanuvchi_ismi =='admin':
    #     print('Xush kelibsiz,'+foydalanuvchi_ismi.title())
    # else:
    #     print(f'Xush kelibsiz,{foydalanuvchi_ismi}')

# (shahriyorga korsatish)   \\\ Foydalanuvchidan 2-ta sonni kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" 
# ekan degan yozuvni konsolga chiqaring
    # sonlar = []
    # for son in range(2):
    #     sonlar.append(input(f'{son+1}-sonni kiriting'))
    # if sonlar[0]==sonlar[1]:
    #     print('Sonlar teng')
    # else:
    #     print('Sonlar teng emas')

# \\\ Foydalanuvchidan istalgana son kirishini so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son",
# agar musbat bo'lsa "Musbat son" degan xabarni chiqaring
    # son = int(input('Istalgan son kiriting:\n>>>>'))
    # if son > 0:
    #     print('Musbat son')
    # else:
    #     print('Manfiy son')

# \\\ Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring.
# Agar son manfiy bo'lsa,"Musbat son kiriting" degan xabarni chiqaring
    # son = int(input('Istalgan son kiriting:\n>>>>'))
    # if son > 0:
    #     print('Ildiz teng=',(son**0.5))
    # else:
    #     print('Musbat son kiriting')