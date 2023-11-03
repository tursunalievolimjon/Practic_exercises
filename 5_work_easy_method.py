# O'zgaruvchilar qiymati
kocha=input('Kocha nomini kiriting:')
mahalla=input('Mahalla nomini kiriting:')
tuman=input('Tuman  nomini kiriting:')
viloyat=input('Viloyat nomini kiriting:')

# standard metod bilan o'zgaruvchilarni chiqarish
print('\nStandard metod bilan o\'zgaruvchilarni chiqarish:\n',kocha,'kochasi,\n',mahalla,'mahallasi,\n'\
      ,tuman,'tumani,\n',viloyat,'viloyati\n')

# f-string yordamida) matn chiqarish
manzil=f'{kocha} kochasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati\n'
print('f-string yordamida) title metodi bilan matn chiqarish(sozlarning bosh hariflari katta boladi):\n',manzil.title())
print('f-string yordamida) capitalize metodi bilan matn chiqarish(birinchi sozning bosh harfi katta boladi):\n',manzil.capitalize())
print('f-string yordamida) upper metodi bilan matn chiqarish(hamma harflar katta boladi):\n',manzil.upper())
print('f-string yordamida lower metodi bilan matn chiqarish(hamma harflar kichkina boladi):\n',manzil.lower())

input()