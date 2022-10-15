
def note(lista1,lista2,start):
    lista3=[lista1[start],]
    stp=start
    for i in lista2:
        stp+=i; 
        if(stp>=0 and stp<=len(lista1)):
            lista3.append(lista1[stp])
        elif(stp<0):
            stp+=len(lista1)
            lista3.append(lista1[stp])
        elif(stp>=len(lista1)):
            stp-=len(lista1)
            lista3.append(lista1[stp])

    print(lista3)

if __name__ == '__main__':
    lista1=["do", "re", "mi", "fa", "sol"]
    lista2=[1,-3, 4, 2]
    start=2
    note(lista1,lista2,start)