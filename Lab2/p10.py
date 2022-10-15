def mat(matrice):
    caine=[[]*len(matrice) for i in range (len(matrice))]
    for i in range(0,len(matrice)):
      for j in range(0,len(matrice[0])):
        caine[i].append(matrice[j][i])
    
    print (caine)



if __name__=='__main__':
    matrice=[[1,2,3],["a","b","c"],[5,6,7]]
    mat(matrice)