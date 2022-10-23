def operat(*seturi):
     dictionar={}
     for i in range(0,len(seturi) - 1):
        dictionar[str(seturi[i]) + " | " + str(seturi[i + 1])] = seturi[i].union(seturi[i + 1])
        dictionar[str(seturi[i]) + " & " + str(seturi[i + 1])] = seturi[i].intersection(seturi[i + 1])
        dictionar[str(seturi[i]) + " - " + str(seturi[i + 1])] = seturi[i].difference(seturi[i + 1])
        dictionar[str(seturi[i + 1]) + " - " + str(seturi[i])] = seturi[i + 1].difference(seturi[i])
     return dictionar   

if __name__=='__main__':
    print(operat({1 , 2} , {2 , 3}))