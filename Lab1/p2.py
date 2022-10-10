def voc(string):
    contr=0
    for i in range (0,len(string)):
        if string[i] in 'aeiouAEIOU':
            contr+=1
    return contr

if __name__ == '__main__':
   
    str = str(input("mesaj: "))
    var = voc(str)
    print (var)