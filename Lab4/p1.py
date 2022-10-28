import os

def f(dir_path):
    vect=[]
    l=os.listdir(dir_path)#listdire=listeaza fisierele din director(google)
    for file in l:
        if os.path.isfile(file):
            vect.append(os.path.splitext(file)[1]) #os.path.splittext desparte extensia de numele fisierului(google)
    return sorted(set(vect))

print(f("."))