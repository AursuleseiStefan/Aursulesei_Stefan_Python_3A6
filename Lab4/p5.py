import os



def cautare(target,to_search):
    listaFis=[]
    try:
        if os.path.isfile(target):
            f=open(target,"r")
            if to_search in f.read():
                listaFis.append(target)
            f.close()
            return listaFis
        elif os.path.isdir(target):
            for root,dirs,files in os.walk(target): #parcurgere recursiva
                for file in files:
                    currentFile=os.path.join(root,file) #currentFile=root+os.sep+file
                    f = open(currentFile,"r")
                    if to_search in f.read():
                        listaFis.append(file)
                    f.close()
            return listaFis
        else: raise ValueError("nu este nici fisier nici director")
    except Exception as e:
        print(e)


if __name__=="__main__":
    print(cautare("C:/Users/aursu/Desktop/pitt","txt"))