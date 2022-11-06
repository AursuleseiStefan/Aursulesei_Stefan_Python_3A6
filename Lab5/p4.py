def my_function(*x,**y):
    ret=[]
    print(x)
    for i in list(x) + list(y.values()):
        if isinstance(i,dict) and len(i.keys())>=2:
            check=False
            for k,v in i.items():
                if isinstance(k,str) and len(k)>=3:
                    check=True
            if check==True:
                ret.append(i)
    return ret

print(my_function( {1: 2, 3: 4, 5: 6}, 

 {'a': 5, 'b': 7, 'c': 'e'}, 

 {2: 3}, 

 [1, 2, 3],

 {'abc': 4, 'def': 5},

 3764,

 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

 test={1: 1, 'test': True}))

