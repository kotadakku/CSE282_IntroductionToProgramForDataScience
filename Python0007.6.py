import numpy as np
c=np.random.randint(20, size=50)
bool_idx = (c > 5)&(c<10)
b=c[bool_idx]
print(b)
