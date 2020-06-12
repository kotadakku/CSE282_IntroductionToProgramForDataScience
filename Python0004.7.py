import math
n=int(input("Nhập n:"))
n=n-1
def Tohop(k,n):
    return int((math.factorial(n)/(math.factorial(k)*math.factorial(n-k))))
if n>=0:
    
    for i in range(0,n+1):
        print()
        for j in range(0,i+1):       
            print(Tohop(j,i),"  ",end='')

