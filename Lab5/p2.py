def p2(*args,**kargs):
    sum = 0
    for elem in kargs.items():
        sum+=elem[1]
    return sum


if __name__=="__main__":
 print(p2(1,2,c = 3,d = 4))
 x=lambda *args, **kargs : sum(kargs.values())
 print(x(1,2,c=3,d=4))