matn = 'Eng katta son'
def katta_son(son1,son2):
    '''Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya'''
    if son1 > son2:
        print(f'{matn} {son1}')
    elif son1 < son2:
        print(f'{matn} {son2}')
    else:
        print('Sonlar teng')
katta_son(son1=int(input('1-chi sonni kiriting:')),
          son2=int(input('2-chi sonni kiriting:'))
          )
