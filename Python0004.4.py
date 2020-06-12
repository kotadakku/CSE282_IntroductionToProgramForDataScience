l1=list([0,1,1])
n=int(input("Nhập n: "))
x1=1
x2=1
while x2<n:
    x3=x1+x2
    x1=x2
    x2=x3
    l1.append(x3)
print(l1)
