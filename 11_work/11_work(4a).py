### 11_work(4a)

mahsulotlar = ['telefon','noutbuk','kompyuter','televizor','playstation','naushnik','zaryadnik','sichqoncha','battareya','monitor']
savat = []
print('Savatga 5-ta mahsulot qo\'shing')
for son in range(5):
    savat.append(input(f'Savatga {son+1}-mahsulotni qo\'shing:'))    
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f'Do\'konimizda {mahsulot} bor')
    elif mahsulot not in mahsulotlar:
        print(f'Do\'konimizda {mahsulot} yo\'q')
    else:
        print('Savatingiz bo\'sh')