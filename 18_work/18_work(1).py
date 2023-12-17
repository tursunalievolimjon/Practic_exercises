print('Buyurtmalar qabul qiluvchi dastur')
buyurtmalar = []
while True:
    savol = input('Buyurtma nomini kiriting:')
    buyurtmalar.append(savol)
    dastur = input('Yana qoshasizmi(dasturni toxtatish uchun "stop" deb yozing):').lower()
    if dastur == 'stop':
        break
print('Buyurtmalar ro\'yhati:')
for buyurtma in buyurtmalar:
    print(buyurtma.title())