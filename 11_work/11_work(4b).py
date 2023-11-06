### 11_work(4b)

mahsulotlar = ['telefon','noutbuk','kompyuter','televizor','playstation','naushnik','zaryadnik','sichqoncha','battareya','monitor']
savat = []
bor_mahsulotlar = []
mavjud_emas = [] 
for i in range(5):
    savat.append(input(f'Savatga {i+1}-chi mahsulotni qo\'shing: '))
for i in savat:
    if i in mahsulotlar:
        bor_mahsulotlar.append(i)
    if i not in mahsulotlar:
        mavjud_emas.append(i)
if len(mavjud_emas)>0:    
    print('Do\'konimizda quyidagi mahsulotlar yo\'q:')
for i in mavjud_emas:
    print(i)
if len(mavjud_emas)==0:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")