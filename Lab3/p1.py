def intersectie(lista1, lista2):
    return list(set(lista1) & set(lista2))
 
def reuniune(lista1, lista2):
    lista = sorted(lista1 + lista2)
    return lista

def scadere1(lista1, lista2):
    lista = list(set(lista1) - set(lista2))
    return lista

def scadere2(lista1, lista2):
    lista = list(set(lista2) - set(lista1))
    return lista

if __name__ == '__main__':
    lista1 = [1,2,3,4,5]
    lista2 = [2,3,4,5,6,7]
    print(intersectie(lista1, lista2))
    print(reuniune(lista1, lista2))
    print(scadere1(lista1,lista2))
    print(scadere2(lista1,lista2))