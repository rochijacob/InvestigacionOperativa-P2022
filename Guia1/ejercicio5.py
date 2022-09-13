import numpy as np

a = [[1, 2, 0],
[3, 0, 4],
[1, 0, 3]]

a = np.array(a)

print(a[0][0] == a[0,0]) #Me fijo si son iguales

print(a[:,1] )

print(a[1] == a[1,:] )

print(a[:, -1])