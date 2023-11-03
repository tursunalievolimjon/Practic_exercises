# Kamida 5 elementdan iborat ismlar degan ro'yhat tuzing, va ro'yhatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ['olimjon','shahriyor','abdurashid','muhammadaziz','islomjon']
for ism in ismlar:
    print('Assalomu alaykum',ism.capitalize())
print('Sizni 18 kuni bolib o\'tadigan bazmga taklif etamiz')
# \
# Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring(n o'rniga kod necha 
# marta takrorlanganini yozing)     ?
# print(f"Kod {len(ismlar)} marta takrorlandi")


# 10 dan 100 gacha bo'lgan toq so'nlar ro'yhatini tuzing. Ro'yhatning xar bir elementining kubini yangi qatordan konsolga chiqaring
# for sonlar in range(11,100,2):
#     print(sonlar**3)


# Foydalanuvchidan 5-ta eng sevimli kinolarini kiritishni so'rang, va kinolar degan ro'yhatga saqlab oling
# Natijani konsolga chiqaring
# kinolar = []
# print('5 ta eng sevimli kinoingizni kiriting:')
# for son in range(5):
#     kinolar.append(input(f'{son+1} kinoingizni kiriting:'))
# print('>>>>')
# for kino in kinolar:
#     print(kino.capitalize())


# Foydalanuvchidan bugun nechta odam bilan uchrashganini so'rang, va har bir suhbatlashgan odamning 
# ismini birma-bir so'rab ro'yhatga yozing
# Ro'yhatni konsolga chiqaring
# miqdor = int(input('Bugun necha kishi bn suhbar qildingiz?>>>>'))
# odamlar = []
# for son in range(miqdor):
#     odamlar.append(input(f'{son+1}-suhbat qilgan odamingiz kim edi: '))
# print(odamlar)