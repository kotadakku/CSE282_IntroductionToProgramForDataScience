a=int(input("Nhập vào số A: "))
k=0     
for d in range(2,a):
    if a/d==a//d:
        k=k+1
if k>0:
    print("%a không là số nguyên tố" %a)     
else: 
    print("%a là số nguyên tố" %a)     
  




