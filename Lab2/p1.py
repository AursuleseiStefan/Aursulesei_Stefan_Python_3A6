fibona=[]
def Fibo(n):
    if(n==2 or n==1):
        return 1
    elif(n==0):
        return 0
    else:
        for i in range(0,n):
            if(i==0):
                fibona.append(0)
            elif(i==2 or i==1):
                fibona.append(1)
            elif(i>2):
                fibona.append(fibona[i-1]+fibona[i-2])
    return fibona

if __name__ == '__main__':
    print (Fibo(9))