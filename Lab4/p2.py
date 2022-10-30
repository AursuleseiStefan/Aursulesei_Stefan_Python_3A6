import os

def funfis(dir,fis):
    varptopen = open(fis,"a")#"a" pentru ca programul sa scrie la finalul sirului
    varnumefis = os.listdir(dir)#listeaza fisele din director(google)
    for i in varnumefis:
        if i.startswith("A"):
            varptopen.write(os.path.abspath(i)+"\n")#scrie in fisier path absoul al fisierului care incepe cu A

    varptopen.close()
    print("Am scris in fisier")


if __name__ == "__main__":
    funfis("C:/Users/aursu/Desktop","C:/Users/aursu/Desktop/folderptpython/nume.txt")
