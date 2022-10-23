def comp(dict1,dict2):
    rez=[]
    if len(dict1) != len(dict2):
        return False
    for k,v in dict1.items(): #k cheie,v valoare
        if (k,v) not in dict2.items():
            return False
        else:
            rez.append((k,v))
    if len(rez)==len(dict1):
        return True
    return False

if __name__=='__main__':
    dict1={"ana":3}
    dict2={"anu":3}
    dict3={"ana":4}
    dict4={"ana":3}
    print(comp(dict1,dict2))
    print(comp(dict1,dict3))
    print(comp(dict1,dict4))