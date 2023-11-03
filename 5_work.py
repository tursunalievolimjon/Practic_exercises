# O'zgaruvchilar qiymati
kocha=input('Kocha nomini kiriting:')
mahalla=input('Mahalla nomini kiriting:')
tuman=input('Tuman  nomini kiriting:')
viloyat=input('Viloyat nomini kiriting:')

# standard metod bilan o'zgaruvchilarni chiqarish
print('\nStandard metod bilan o\'zgaruvchilarni chiqarish:\n',kocha,'kochasi,\n',mahalla,'mahallasi,\n'\
      ,tuman,'tumani,\n',viloyat,'viloyati\n')


# f-string yordamida) title metodi bilan matn chiqarish 1-chi uslubi(bosh hariflar katta boladi)
manzil=f'{kocha.title()} kochasi, \n{mahalla.title()} mahallasi, \n{tuman.title()} tumani, \n{viloyat.title()} viloyati\n'
print('f-string yordamida) title metodi bilan matn chiqarish 1-chi uslubi(sozlarning bosh hariflari katta boladi):\n',manzil)
# f-string yordamida) title metodi bilan matn chiqarish uchun 2-chi uslubi
manzil=f'{kocha} kochasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati\n'
print('f-string yordamida) title metodi bilan matn chiqarish 2-chi uslubi:\n',manzil.title(),\
      '\ntitle metodining 2-ta uslubi')
# title metodining 2-ta uslubi


# f-string yordamida) capitalize metodi bilan matn chiqarish 1-chi uslubi(bosh hariflar katta boladi)
manzil=f'{kocha.capitalize()} kochasi, \n{mahalla.capitalize()} mahallasi, \
    \n{tuman.capitalize()} tumani, \n{viloyat.capitalize()} viloyati\n'
print('\nf-string yordamida) capitalize metodi bilan matn chiqarish 1-chi uslubi(birinchi sozning bosh harifi katta boladi):\n',manzil)
# f-string yordamida) capitalize metodi bilan matn chiqarish 2-chi uslubi
manzil=f'{kocha} kochasi, \n{mahalla} mahallasi, \
    \n{tuman} tumani, \n{viloyat} viloyati\n'
print('f-string yordamida) capitalize metodi bilan matn chiqarish 2-chi uslubi:\n'\
      ,manzil.capitalize(),'\ncapitalize metodining 2-ta uslubi')
# capitalize metodining 2-ta uslubi


# f-string yordamida) upper metodi bilan matn chiqarish 1-chi uslubi(hamma hariflar katta boladi)
manzil=f'{kocha.upper()} kochasi, \n{mahalla.upper()} mahallasi, \n{tuman.upper()} tumani, \n{viloyat.upper()} viloyati\n'
print('\nf-string yordamida) upper metodi bilan matn chiqarish 1-chi uslubi(hamma hariflar katta boladi):\n',manzil)
# f-string yordamida) upper metodi bilan matn chiqarish 2-chi uslubi
manzil=f'{kocha} kochasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati\n'
print('f-string yordamida) upper metodi bilan matn chiqarish 2-chi uslubi:\n',manzil.upper(),\
      '\nupper metodining 2-ta uslubi')
# upper metodining 2-ta uslubi


# f-string yordamida) lower metodi bilan matn chiqarish 1-chi uslubi(hamma hariflar kichik boladi)
manzil=f'{kocha.lower()} kochasi, \n{mahalla.lower()} mahallasi, \n{tuman.lower()} tumani, \n{viloyat.lower()} viloyati\n'
print('\nf-string yordamida) lower metodi bilan matn chiqarish 1-chi uslubi(hamma hariflar kichik boladi):\n',manzil)
# f-string yordamida) lower metodi bilan matn chiqarish 2-chi uslubi
manzil=f'{kocha} kochasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati\n'
print('f-string yordamida) lower metodi bilan matn chiqarish 2-chi uslubi:\n',manzil.lower(),'\nlower metodining 2-ta uslubi')
# lower metodining 2-ta uslubi

input()