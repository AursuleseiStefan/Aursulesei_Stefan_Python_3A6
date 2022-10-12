lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

nrprime=[]

for i in lista:
    contor=0

    for j in range(1,i):
        if i%j==0:
            contor+=1
    if contor==1:
        nrprime.append(i)

if __name__ == '__main__':
    print(nrprime)