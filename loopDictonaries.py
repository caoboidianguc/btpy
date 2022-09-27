nested = [1,2, ['a','b','c'],['d','e'],['f','g','h'] ]

for item in nested:
    print('level1')
    if type(item) is list:
        for chara in item:
            print('         level 2: {}'.format(chara))
    else : 
        print('     ',item)