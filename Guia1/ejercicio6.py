import numpy as np

a = [2, 10, 16, 2, 4, 12, 24, 100]
b = [5, 2, 5, 2, 1, 2, 1, 0.5]

#Zip hace lo mismo que la linea de abajo

#zipped_lists = zip(a, b)

#multiply = [x* y for (x, y) in zipped_lists]


multiply = [a[i]*b[i] for i in range(len(a))] #Solo funciona si tienen la misma longitud

sum = 0

for i in multiply:
  sum = sum + i

print('Artesanalmente:', sum)


#Sumando con numpy en vez de zip
numpy_prod = np.multiply(a, b)
numpy_add = np.sum(numpy_prod)

print('Numpy sin convertir en array:', numpy_add)

#Con dot

np_a = np.array(a)
np_b = np.array(b)

np_dot = np.dot(np_a, np_b)

print('Numpy con dot:', np_dot)