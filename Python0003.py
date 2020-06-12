import math
a=int(input("Nhập A:"))
b=int(input("Nhập B:"))
if a==0 and b==0:
    print("UCLN=0, BCLN=0")
else:
    print(math.gcd(a,b))
    print((a*b)/math.gcd(a,b))
