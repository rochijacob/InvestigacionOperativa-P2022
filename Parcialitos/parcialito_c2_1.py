#Programacion Entera
import picos
import numpy as np

P = picos.Problem()

#Funcion Objetivo - minimizar el tiempo para hacer estas tareas

t = np.array([[4.5, 7.8, 3.6, 2.9, 4.9, 7.2, 4.3, 3.1]])

x = picos.BinaryVariable('x', 8)

P.set_objective('min', x|t)

#Restriccion de que cada uno tenga solo dos obligaciones

P.add_constraint(x[0] + x[1] + x[2] + x[3] == 2)
P.add_constraint(x[4] + x[5] + x[6] + x[7] == 2)

P.solve(solver='glpk')

print('valor de P', P.value)

print('valor de x', x)