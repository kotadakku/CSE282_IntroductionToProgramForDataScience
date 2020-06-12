a=int(input("Nhập A: "))
b=int(input("Nhập B: "))
for j in range(a,b+1):
    k=0
    for i in range(2,j):
        if j/i==j//i:
            k=k+1
    if k==0:
        print(j)

           
