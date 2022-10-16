def spectatori(matrice):
  listaTuple=list()
  for i in range(0,len(matrice[0])):
    for j in range (len(matrice)-1,0,-1):#-1 bcz merge invers
      ok=False
      for k in range(j-1,-1,-1):
        if(matrice[j][i]<=matrice[k][i]):
          tuplu=(j,i)
          listaTuple.append(tuplu)
          break
  return listaTuple

if __name__=='__main__':
  matrice=[
            [1,2,3,2,1,1],
            [2,4,4,3,7,2],
            [5,5,2,5,6,4],
            [6,6,7,6,7,5]]
  print(spectatori(matrice))