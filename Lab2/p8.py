def funct(x=1,lista=[],flag=True):
  dictionar={}
  i=0 #i este cheia dictionarului
  for cuvant in lista:
    i+=1
    listacaractere=[]
    for j in range(len(cuvant)):
      if ord(cuvant[j])%x==0 and flag is True:#ord=codul ASCII(google)
        listacaractere.append(cuvant[j])
      elif ord(cuvant[j])%x!=0 and flag is False:
        listacaractere.append(cuvant[j])
    dictionar[cuvant]=listacaractere
  return list(dictionar.values())

if __name__=='__main__':
  x=2
  lista=['test','hello','lab002']
  flag=False
  print(funct(x,lista,flag))