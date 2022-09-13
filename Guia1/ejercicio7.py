import numpy as np

a = [[1, 2, 0],[3, 0, 4],[1, 0, 3]]
b = [[3, 1, 1], [1, 2, 0], [2, 4, 1]]

#Resultado de la multiplicacion
#[5  5  1]
#[17 19 7]
#[9  13 4]

#Transformo a arrays

a = np.array(a)
b = np.array(b)

#Con For Loop

result = [] # array donde voy a ir mandando las rows que genero
for i in range(len(a)): #voy a tener 3 rows

    row = [] # la row que voy a generar
    for j in range(len(b[0])):
        
        product = 0 
        for v in range(len(a[i])): #para cada valor en a[0]
            product += a[i][v] * b[v][j]
        row.append(product) 
        
    result.append(row) 


print('Con for loop', result)

#Multilplicacion con numpy

print('Con Numpy', a@b)