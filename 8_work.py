# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# davlatlar = ['Koreya','Yaponiya','Antaliya','Germaniya']
# print('O\'zingizga ma\'lum davlatlarning ro\'yxatini tuzing va ro\'yxatni konsolga chiqaring:',davlatlar,'\n')

# Ro'yhatning uzunligini konsolga chiqaring
# print('Ro\'yhatning uzunligini konsolga chiqaring:',len(davlatlar),'\n')

# sorted() funktsiyasi yordamida ro'yhatni tartiblangan holda konsolga chiqaring
# print('sorted() funktsiyasi yordamida ro\'yhatni tartiblangan holda konsolga chiqaring:',sorted(davlatlar),'\n')

# sorted() funktsiyasi yordamida ro'yhatni teskari tartibda konsolga chiqaring
# print('sorted() funktsiyasi yordamida ro\'yhatni teskari tartibda konsolga chiqaring:',sorted(davlatlar,reverse=True),'\n')

# Asl ro'yhatni qaytadan konsolga chiqaring
# print('Asl ro\'yhatni qaytadan konsolga chiqaring:',davlatlar,'\n')

# reverse() metodi yordamida ro'yhatni ortidan boshlab chiqaring
# davlatlar.reverse()
# print('reverse() metodi yordamida ro\'yhatni ortidan boshlab chiqaring:',davlatlar,'\n')

# sort() metodi yordamida avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring
# davlatlar.sort()
# print('sort() metodi yordamida alifbo tartibida konsolga chiqaring:',davlatlar,'\n')

# sort() metodi yordamida alifboga teskari tartibda konsolga chiqaring
# davlatlar.sort(reverse=True)
# print('sort() metodi yordamida alifboga teskari tartibda konsolga chiqaring:',davlatlar,'\n')

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yhatini tuzing
# sonlar = list(range(120,1200,2))
# print('120 dan 1200 gacha bo\'lgan juft sonlar ro\'yhatini tuzing:',sonlar,'\n')

# Ro'yhatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# print('Ro\'yhatdagi sonlar yig\'indisini hisoblang va konsolga chiqaring:',sum(sonlar),'\n')

# Ro'yhatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# print('Eng katta son =',max(sonlar),'\nEng kichik son =',min(sonlar))
# print('Ro\'yhatdagi eng katta va eng kichik son o\'rtasidagi ayirmani hisoblang va konsolga chiqaring:',max(sonlar)-min(sonlar),'\n')

# Ro'yhatdagi elementlar sonini hisoblang
# print('Ro\'yhatdagi elementlar sonini hisoblang:',len(sonlar),'\n')

# Ro'yhatning boshidan, o'rtasidan va oxiridan 20-ta qiymatni konsolga chiqaring
# print(sonlar[:20],'\n',sonlar[260:280],'\n',sonlar[-20:])


# taomlar degan ro'yhat yarating va ichiga istalgan 5-ta taomni kiriting
taomlar = ['saryoq','kolbasa','osh','mostava','goshli non']

# nonushta degan yangi ro'yhatga taomlar dan nusxa oling
nonushta = taomlar[:]

# Yangi ro'yhatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qoshimcha 2-ta taom qo'shing
del nonushta[2]
nonushta.remove('mostava')
del nonushta[2]

nonushta.append('choko-cream')
nonushta.insert(1,'butter-bread')
print('Taomlar:',taomlar,'\nNonushta:',nonushta)

# Yuqoridagi nonushta ro'yhatini o'zgarmas ro'yhatga aylantiring va nonushta[0] = 'qaymoq va non' deb qiymat berib ko'ring
nonushta = tuple(nonushta)
nonushta[0] = 'qaymoq va non'
print(nonushta)