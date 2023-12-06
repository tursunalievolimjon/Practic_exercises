kinolar = {'islomjon':{'kinolar':['anime','marvel','youtube-shorts']},
           'shahriyor':{'kinolar':['None']},
           'abdurashid':{'kinolar':['ip-man','djeki-chan','forsaj']}}
#
for ism,info in kinolar.items():
    print(f'{ism.title()}-ning sevimli kinolari:')
    for k in info['kinolar']:
        print(f'{k.title()}')