### 11_work(6)

# son = int(input('Istalgan son kiriting:')) 
# if son%2==0:
#     print(f'{son} soni 2 ga qo\'ldiqsiz bo\'linadi')
# if son%3==0:
#     print(f'{son} soni 3 ga qo\'ldiqsiz bo\'linadi')
# if son%4==0:
#     print(f'{son} soni 4 ga qo\'ldiqsiz bo\'linadi')
# if son%5==0:
#     print(f'{son} soni 5 ga qo\'ldiqsiz bo\'linadi')
# if son%6==0:
#     print(f'{son} soni 6 ga qo\'ldiqsiz bo\'linadi')
# if son%7==0:
#     print(f'{son} soni 7 ga qo\'ldiqsiz bo\'linadi')
# if son%8==0:
#     print(f'{son} soni 8 ga qo\'ldiqsiz bo\'linadi')
# if son%9==0:
#     print(f'{son} soni 9 ga qo\'ldiqsiz bo\'linadi')
# if son%10==0:
    # print(f'{son} soni 10 ga qo\'ldiqsiz bo\'linadi')

son = int(input('Istalgan son kiriting:'))
for i in range (2,11):
    if son%i==0:
        print(f'{son} soni {i} ga qo\'ldiqsiz bo\'linadi')