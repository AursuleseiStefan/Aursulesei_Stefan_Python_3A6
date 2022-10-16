def verifpalindrom(numar):
  copie=numar
  a=0
  while(numar):
    a=a*10+(numar%10)
    numar=numar//10
  if(copie==a):
    return True
  else:
    return False 

def listapal(lista):
  numarpalin=0
  maxnumar=0
  for i in lista:
    if(verifpalindrom(i)):
        numarpalin+=1
        if(maxnumar<i):
          maxnumar=i
  return numarpalin,maxnumar


if __name__=='__main__':
  lista=[121,222,212,13,42,844232448]
  print(listapal(lista))
