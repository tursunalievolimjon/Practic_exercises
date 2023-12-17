def bolinish_alomatlari(x):
    for y in range(2,11):
        if x % y ==0:
            print(f'{x} soni {y} qoldiqsiz bo\'linadi')
bolinish_alomatlari(x=int(input('Son kiriting:')))