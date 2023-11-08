### \\\ 4-chi mashq(b)
#\
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))    # 1)\-backslash qoyilmagan edi
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)    # 2) bor_mahsulotlar o'zgaruvchisiga qushilayotgan /
# mahsulot nomli o'zgaruvchida "u" harfi tushib qolgan edi
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)     # 3) "for" tsikli orqaga surilgan edi va if funktsiyasi dan tashqarida edi
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
#/
### /// 3-ta xato mavjud edi.