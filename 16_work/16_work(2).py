mashhurlar4 = {'ilon musk':{'kashfiyotlar':['tesla','spaceX','neurolink']},
            'bill gates':{'kashfiyotlar':['microsoft','xbox']},
            'tim kuk':{'kashfiyotlar':['iphone','apple watch','macbook']},
            'pavel durov':{'kashfiyotlar':['telegram','vkontakte']}}
#
for ism,info in mashhurlar4.items():
    print(f'{ism.title()}-ning kashfiyotlari:')
    for k in info['kashfiyotlar']:
        print(k.title())