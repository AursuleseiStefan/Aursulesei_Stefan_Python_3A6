def ex5(lista):
    listaNoua = list()
    for i in lista:
        if isinstance(i,int) or isinstance(i,float):
            listaNoua.append(i)
    return listaNoua

print(ex5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
lista=[1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]
x=[i for i in lista if isinstance(i,int) or isinstance(i,float)]
print(x)
