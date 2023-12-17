print('Mahsulotlar va ularning narhini ro\'yhatini yaratuvchi dastur')
e_bozor = {}

while True:
    mahsulot = input('Mahsulot nomini kiriting:')
    narh = int(input(f'{mahsulot.title()}ning narhini kiriting:'))
    
    e_bozor[mahsulot] = narh
    
    savol = input('Yana mahsulot qoshasizmi?(ha/yoq)\n>>>>')
    if savol == 'yoq':
        break
print('Mahsulotlar ro\'yhati:')
for key, value in e_bozor.items():
    print(f'{key.title()}ning narhi {value}so\'m')