# ismlar degan ro'yhat yarating va kamida 3-ta yaqin do'stingizni ismini kiriting
# Ro'yhatdagi har bir do'stingizga qisqa habar yozib konsolga chiqaring:
ismlar = ['Shahriyor','Islomjon','Abdurashid']
print('Salom',ismlar[0]+', bugun choyhona bormi?\n' + ismlar[1]+', choyhonaga boramizmi?\n')

# sonlar deb nomlangan ro'yhat yarating va ichiga turli sonlarni yuklang(musbat,manfiy,butun,o'nlik)
# Yuqoridagi ro'yhadagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yhatdagi ba'zi /
# \ sonlarning qiymatini o'zgartiring, bazilarini esa almashtiring.
sonlar = [15,-15,20.0]
print('Kiritilgan sonlar',sonlar,'\n')

print('Sonlar ustida arifmetik amallar:\n15 + 15 =',sonlar[0]+sonlar[0],'\n-15 + 20.0 =',sonlar[1]+sonlar[2],'\n')

sonlar.append(20)
print('Append metodi bilan qushilgan 20 soni',sonlar,'\n')
sonlar.insert(1,35)
print('Insert metodi bilan qushilgan 35 soni - 1chi uringa',sonlar)

# \ t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng /
# \ ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
t_shahslar = ['Al-Xorazmiy','Al-Beruniy','Amir Temur']
z_shahslar = ['Ahad Qayum','Alisher Uzoqov','Munisa Rizaeva']
print('\nMen tarixiy shahslardan',t_shahslar.pop(2),'bilan,\nzamonaviy shahslardan \
esa',z_shahslar.pop(1),'bilan suhbat qilishmi istar edim\n')

# \ friends nomli bo'sh ro'yxat tuzing va unga .append() /
# \ yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append('Shahriyor')
friends.append('Ruhshona')
friends.append('Muhammadaziz')
friends.append('Abdurashid')
friends.append('Bobur')
friends.append('Islomjon')
print('append() metodi yordamida friends o\'zgaruvchisiga qushilgan ismlar',friends,'\n')

# Yuqoradagi ro'yhatdan kela olmaydigan odamlarni .remove() metodi yordamida o'chirib tashlang.
friends.remove('Bobur')
friends.remove('Muhammadaziz')
friends.remove('Abdurashid')
print('remove() metodi yordamida olib tashlangan ismlardan keyingi holat',friends,'\n')

# Ro'yhatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.insert(1,'Nozanin')
friends.insert(2,'Jumanazar')
friends.insert(3,'Otabek')
print('insert() metodi yordamida qushilgan yangi ismlar',friends,'\n')

# \ Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan /
# \ do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing /
mehmonlar = [friends.pop(0),friends.pop(1),friends.pop(2)]
mehmonlar.append('Otabek')
mehmonlar.append('Ruhshona')
mehmonlar.append('Islomjon')
print(mehmonlar)