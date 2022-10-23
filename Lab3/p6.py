def tupla(lista) :
     a = set(lista)
     dubla = len(lista) - len(a)
     tupl = (a , dubla)
     return tupl

print(tupla([1 , 2 , 3 , 4, 3 , 4]))