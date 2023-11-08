### \\\ 2-chi mashq
#\
yosh = int(input("Yoshingiz nechida?"))     # 1)kiritilgan malumot int(butun son)-ga uzgartirilmagan edi
if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:     # 2)shart dan keyin ikki-nuqta qolib qetgan
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")    # 3)print funktsiyasi oldinga surilgan edi
#/
### /// 3-ta xato mavjud edi