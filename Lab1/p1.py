def div(x,y):
    if(x==y):
        return x
    if(x==0):
        return x
    if(y==0):
        return y
    if x>y:
        return div(x-y,y)   
    else:
        return div(x,y-x)

if __name__ == '__main__':
    vector = []
    nrelem=int (input ("introdu nr elem: "))
    for i in range (0,nrelem):
        element = int (input())
        vector.append(element)
    if nrelem<2:
        print ("cel putin 2 elemente trb")
    elif nrelem==2:
       vargcd2= div(vector[0],vector[1])
    else:
        varvect=vector[0]
        for i in range(1,nrelem):
            varvect=div(varvect,vector[i])
    print("rez este: ",varvect)