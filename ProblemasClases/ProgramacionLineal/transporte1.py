import picos
import numpy as np

P = picos.Problem()
X = picos.RealVariable('X', (3,4), lower = 0)

# Matriz de costo
C = picos.Constant('C', [[8,6,10,9], [9,12,13,7], [14,9,16,5]])

# Funcion objetivo a minimizar
# Producto escalar: multiplica elemento a elemento y suma todo
P.set_objective('min', C|X)

# Condiciones de oferta
P.add_constraint(X[0,0] + X[0,1] + X[0,2] + X[0,3] <= 35)  # s_1
P.add_constraint(X[1,0] + X[1,1] + X[1,2] + X[1,3] <= 50)  # s_2
P.add_constraint(X[2,0] + X[2,1] + X[2,2] + X[2,3] <= 40)  # s_3

# Condiciones de demanda
# Como el problema esta balanceado puedo poner igualdades
P.add_constraint(X[0,0] + X[1,0] + X[2,0] == 45)  # d_1
P.add_constraint(X[0,1] + X[1,1] + X[2,1] == 20)  # d_2
P.add_constraint(X[0,2] + X[1,2] + X[2,2] == 30)  # d_3
P.add_constraint(X[0,3] + X[1,3] + X[2,3] == 30)  # d_4

P.solve()
print(X)
print(P.value)

# Formas equivalentes de escribir el producto escalar
print(C|X)
print(picos.sum(C^X))
print(picos.trace(C*X.T))