def gasirerime(listacuv):
    rime = {}
    for word in listacuv:
        if word[-2:] in rime:
            rime[word[-2:]] += [word]
        else:
            rime[word[-2:]] = [word]
    return list(rime.values())

if __name__=="__main__":
  listacuv = ['ana', 'banana', 'carte', 'arme', 'parte']
  result = gasirerime(listacuv)
  print("rimele sunt: ", result)
