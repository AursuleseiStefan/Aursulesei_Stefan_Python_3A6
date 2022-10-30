import os


def f(my_path):
    if os.path.isfile(my_path):
        f=open(my_path,"r")
        cuvinte=f.read()
        print(cuvinte[-20:])#ultimele 20 cuv
    elif os.path.isdir(my_path):
        dicti={}
        for root,dirs,files in os.walk(my_path): #parcurgere recursiva
            for fis in files:
                extens=os.path.splitext(fis)[1][1:]#citeste fara punct extensia
                if extens in dicti:
                    dicti[extens]+=1
                else:
                    dicti[extens]=1
        listaTuple=list(zip(dicti.keys(),dicti.values()))#zip atribuie ficarei key o val din dictionar
        listaTuple.sort(key=lambda i:i[1],reverse=True)#sorteaza tuplele in functie de aparitii//revrse-descrescator
        print(listaTuple)


if __name__=="__main__":
    f("C:/Users/aursu/Desktop")