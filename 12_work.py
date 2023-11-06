### XATOLAR BILAN ISHLASH ###



### \\\ 1-chi mashq
#\
# son = float(input("Juft son kiriting: "))   # 1)oxirida 1-ta qavis qolib ketgan edi
# if son%2==0:
#     print("Rahmat!")  # 2)string malumot-di konsolga chiqarishda ikki xil tirnoqlar ishlatilgan edi(boshida " va oxirida ')
# else:
#     print("Bu son juft emas.")    # 3)malumotni konsolga chiqarishda 1-ta ortiqcha qavis ishlatilgan edi
#/
# 4)1-chi va 2-chi print_funktsiyasi-da berilgan malumotlar almashib qolgan edi
### /// 4-ta xato mavjud edi


### \\\ 2-chi mashq
#\
# yosh = int(input("Yoshingiz nechida?"))     # 1)kiritilgan malumot int(butun son)-ga uzgartirilmagan edi
# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:     # 2)shart dan keyin ikki-nuqta qolib qetgan
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")    # 3)print funktsiyasi oldinga surilgan edi
#/
### /// 3-ta xato mavjud edi


### \\\ 3-chi mashq
#\
# x = float(input("Birinchi sonni kiriting: "))   # 1)oxirida ) qolib ketgan edi.
# y = float(input("Ikkinchi sonni kiriting: "))   # 2)oxirida ) qolib ketgan edi.
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f'{x}<{y}')   # 3)string malumot-di konsolga chiqarishda ikki xil tirnoqlar ishlatilgan edi(boshida ' va oxirida ").
# else:  # 4)shart dan keyin ikki-nuqta qolib ketgan 
#     print(f"{x}>{y}")
#/
### /// 4-ta xato mavjud edi.


### \\\ 4-chi mashq(a)
#\
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']   # 1) ]-tortburchak qavis qoyilmagan edi.
# savat = []  # savat nomli o'zagaruvchi yozilmagan edi
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# if savat:
#     for mahsulot in savat:  # 2)tsikl dan keyin ikki-nuqta qoyilmagan edi.
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")
#/
### /// 2-ta xato mavjud edi.


### \\\ 4-chi mashq(b)
#\
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))    # 1)\-backslash qoyilmagan edi
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)    # 2) bor_mahsulotlar o'zgaruvchisiga qushilayotgan /
# # mahsulot nomli o'zgaruvchida "u" harfi tushib qolgan edi
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)     # 3) "for" tsikli orqaga surilgan edi va if funktsiyasi dan tashqarida edi
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
#/
### /// 3-ta xato mavjud edi


### \\\ 5-chi mashq
#\
# users = ['alisher1983','aziza','yasina' 'umar']
# login = input("Yangi login tanlang:" )      # 1) kiritilayotgan string malumotda ikki xil tirnoqlar ishlatilgan edi(boshida " va oxirida ')
# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")
#/
### /// 1-ta xato mavjud edi


### \\\ 6-chi mashq
#\
son = int(input("Istalgan butun son kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
#/
### /// Xatolik mavjud emas
