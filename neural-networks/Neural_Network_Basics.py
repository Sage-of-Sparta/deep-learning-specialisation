
#a.shape = (3,4)
#b.shape = (4,1)


import numpy as np

a = np.array([[1,1,1,1],[1,1,1,1],[1,1,1,1]])

b = np.array([[1],[1],[1],[1]])

c = np.zeros((3,4))

for i in range(3):
    for j in range(4):
        c[i][j] = a[i][j] + b[j]
        
print c

print c.shape

