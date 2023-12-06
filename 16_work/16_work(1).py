### \\\ 1_work

mashhurlar4 = {'ilon musk':{'ism':'ilon musk',
                         't_yil':'28 iyun 1971',    # t_yil = tug'ilgan yil
                         't_sh':'pretoriya',    # t_sh = tug'ilgan shahar
                         'yosh':52},
            'bill gates':{'ism':'bill gates',
                          't_yil':'28 oktyabr 1955',
                          't_sh':'sietl',
                          'yosh':68},
            'tim kuk':{'ism':'tim kuk',
                       't_yil':'1 noyabr 1960',
                       't_sh':'mobil',
                       'yosh':63},
            'pavel durov':{'ism':'pavel durov',
                          't_yil':'10 oktyabr 1984',
                          't_sh':'sankt peterburg',
                          'yosh':39}}
#
for ism,info in mashhurlar4.items():
    print(f'{ism.title()}'
          f' {info['t_yil']}-yilda'
          f' {info['t_sh'].title()} shahrida tavallud topgan.'
          f' {info['yosh']}-yoshda')    # yosh = 2023 yil malumot