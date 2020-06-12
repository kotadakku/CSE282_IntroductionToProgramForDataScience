import numpy as np
c=np.random.randn(10,100)
bool_idx =(c>=(-0.5)) & (c<=0.5)
b=c[bool_idx]
print(b)
