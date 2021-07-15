import numpy as np

b = np.array([[1,2,0],[3,4,0],[5,6,0],[7,8,0]])
print(b)
a = np.array([1,2,3,4])
print(a > 2)
print(b[a > 2])


print((a > 2).flatten())
