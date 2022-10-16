def functdeapar(x, *args):
  dictionar={}
  lista_finala=[]
  for i in args:
    for j in i:
      if j in dictionar:
        dictionar[j]+=1
      else:
        dictionar[j]=1
  for cheie,valoare in dictionar.items():#parcurge toti itemi din dictionar(google)
    if(valoare==x):
      lista_finala.append(cheie)
  return lista_finala


if __name__=='__main__':
  x=2
  lista1=[1,2,3]
  lista2=[2,3,4]
  lista3=[4,5,6]
  lista4=[4,1,'test']
  rez=functdeapar(x,lista1,lista2,lista3,lista4)
  print(rez)