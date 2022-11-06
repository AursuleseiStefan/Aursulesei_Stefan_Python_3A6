def ex6(lista):
    l_even = [elem for elem in lista if elem%2==0]
    l_odd = [elem for elem in lista if elem%2==1]
    return list(zip(l_even,l_odd))

if __name__=="__main__":
    print(ex6([1,3,5,2,8,7,4,10,9,2]))