e_bozor = {'ruchka':1500,
           'daftar':4500,
           'penal':15000,
           'lineyka':7000,
           'chiqarg\'ich':3000}     # 5-ta mahsulot

buyurtmalar = []

while True:
    buyurtma = input('Mahsulot buyurtma bering:').lower()
    buyurtmalar.append(buyurtma)
    
    savol = input('Yana mahsulot buyurtma berasizmi?(ha/yoq)\n>>>>')
    if savol == 'yoq':
        break
    
for mahsulot in buyurtmalar:
    if mahsulot in e_bozor:
        print(f'{mahsulot.capitalize()} - {e_bozor[mahsulot]} so\'m')
    else:
        print(f'Bizda {mahsulot.capitalize()} mahsuloti mavjud emas')