import numpy as np
a=np.random.randint(3000, size=100)
b=a[a%2!=0]
print(a)
print(b)
