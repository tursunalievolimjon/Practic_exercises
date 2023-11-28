### \\\ 4_work

r_menu = {'osh':25000,      # r_menu = restaurant menu
          'mastava':15000,  # mahsulotlar narxi taxminiy qoyilgan
          'non':3000,
          'choy':1500,
          'olivie salat':1200,
          'fanta_1l':6000,
          'pepsi_1l':6000,
          'snickers_tort':70000,
          'xot_dog-mini':10000,
          'xot_dog-bolshoy':20000
          }
###
# sorov = []
# print('3-ta taom buyurtma bering:')
# for s in range(1,4):
#     sorov.append(input(f'{s} taom:'))

# menu = []
# for k in r_menu.keys():
#     menu.append(k)
# for t in sorov:
#     if t in menu:
#         print(f'{t.title()} {r_menu[t]} so\'m')
#     else:
#         print(f'Kechirasiz bizda {t} yo\'q')

# print(menu)
# print(sorov)

### \\\ kodlarni qisqartirishga harakart qilib ko'rish kerak
r_menu = {'osh':25000,      # r_menu = restaurant menu
          'mastava':15000,
          'non':3000,
          'choy':1500,
          'olivie salat':1200,
          'fanta_1l':6000,
          'pepsi_1l':6000,
          'snickers_tort':70000,
          'xot_dog-mini':10000,
          'xot_dog-bolshoy':20000
          }
###
sorov = []
print('3-ta taom buyurtma bering:')
for s in range(1,4):
    sorov.append(input(f'{s} taom:'))

for t in sorov:
    if t in r_menu.keys():
        print(f'{t.title()} {r_menu[t]} so\'m')
    else:
        print(f'Kechirasiz bizda {t} yo\'q')
