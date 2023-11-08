### \\\ 3-chi mashq
#\
x = float(input("Birinchi sonni kiriting: "))   # 1)oxirida ) qolib ketgan edi.
y = float(input("Ikkinchi sonni kiriting: "))   # 2)oxirida ) qolib ketgan edi.
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f'{x}<{y}')   # 3)string malumot-di konsolga chiqarishda ikki xil tirnoqlar ishlatilgan edi(boshida ' va oxirida ").
else:  # 4)shart dan keyin ikki-nuqta qolib ketgan 
    print(f"{x}>{y}")
#/
### /// 4-ta xato mavjud edi.