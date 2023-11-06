### 3_work(3)

bir_son = float(input('Birinchi sonni kiriting:\n>>>>'))
ikki_son = float(input('Ikkinchi sonni kiriting:\n>>>>'))
if bir_son==ikki_son:
    print(f'{bir_son} = {ikki_son}')
elif bir_son<ikki_son:
    print(f'{bir_son} < {ikki_son}')
else:
    print(f'{bir_son} > {ikki_son}')