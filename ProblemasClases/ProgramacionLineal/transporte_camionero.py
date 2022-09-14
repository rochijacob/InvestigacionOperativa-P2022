'''
Resolución del problema del camionero (forma larga)
'''

import picos
import numpy as np

P = picos.Problem()
# Las variables de decisión solo pueden ser 0 o 1
# pero en la matriz X puede tener valor negativos por como la armo
X = picos.IntegerVariable('X', (8, 8), lower=0)

C = 0.5*np.array([[0, 400, 950, 800, 0, 0, 0, 0],
              [-400, 0, 0, 0, 1800, 900, 0, 0],
              [-950, 0, 0, 0, 1100, 600, 0, 0],
              [-800, 0, 0, 0, 0, 600, 1200, 0],
              [0, -1800, -1100, 0, 0, -900, 0, 400],
              [0, -900, -600, -1200, 900, 0, 1000, 1300],
              [0, 0, 0, -1200, 0, -1000, 0, 600],
              [0, 0, 0, 0, -400, -1300, -600, 0]])

C = picos.Constant('C', C)

P.set_objective('min', C | X)
# lo mismo: multiplica elemento a elemento y después suma
# P.set_objective(picos.sum(C^X))

# Antisimetria
P.add_constraint(X == -X.T)

# Todos los ceros
P.add_list_of_constraints([X[i, :] == 0 for i in range(8)])

# Condicion de salida
P.add_constraint(picos.sum(X[0, :]) == 1)

# Condiciones de paso
P.add_constraint(picos.sum(X[1, :]) == 0)
P.add_constraint(picos.sum(X[2, :]) == 0)
P.add_constraint(picos.sum(X[3, :]) == 0)
P.add_constraint(picos.sum(X[4, :]) == 0)
P.add_constraint(picos.sum(X[5, :]) == 0)
P.add_constraint(picos.sum(X[6, :]) == 0)

# Condicion de entrada
P.add_constraint(picos.sum(X[7, :]) == -1)

P.solve()

print(X)
print(P.value)