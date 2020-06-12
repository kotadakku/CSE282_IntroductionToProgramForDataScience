n=int(input("Nhập n: "))
for i in range(1,n):
      s=0
      for j in range(1,i):
           if i//j==i/j:
                s=s+j
      if s>i:
          print(i)
      
      
