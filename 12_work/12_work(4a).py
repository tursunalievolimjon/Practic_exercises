### \\\ 4-chi mashq(a)
#\
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']   # 1) ]-tortburchak qavis qoyilmagan edi.
savat = []  # savat nomli o'zagaruvchi yozilmagan edi
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
if savat:
    for mahsulot in savat:  # 2)tsikl dan keyin ikki-nuqta qoyilmagan edi.
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")
#/
### /// 2-ta xato mavjud edi.