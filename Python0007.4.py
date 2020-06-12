import numpy as np
a=np.array([[1,2,3],[8,5,4]])
b = np.array([[1, 2, 3],[4, 5, 6]]) 
c = np.concatenate([a,b], axis=1) 
print(c)
