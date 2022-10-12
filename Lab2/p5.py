def mat(matrice):
    for i in range(0,len(matrice)):
        for j in range (0,len(matrice)):
            if(j<i):
                matrice[i][j]=0
    return matrice

if __name__ == '__main__':
    matrice=[[1, 4, 5], 
    [5, 8, 9],
    [6, 7, 11]]
    print(mat(matrice))