import picos
import numpy as np

P = picos.Problem()

x = picos.IntegerVariable('x', 3, lower = 0) #¿Cuando uso interger variable?
y = picos.BinaryVariable('y', 3)

#Matriz de Costos Fijos
cf = np.array([[80000, 40000, 30000]]) #Matriz & Costo fijo expresado en miles

#Matriz de Costos Variables
cv = np.array([[20, 25, 30]])

#Matriz de restriccion a la produccion
prod = np.array([[6000, 7000, 6000]])


#Funcion Objetivo
P.set_objective('min', cf*y + cv*x)


#Restricciones
P.add_constraint(sum(x) == 12000)
P.add_constraint(x<=prod)
P.add_list_of_constraints(x[i] <= prod[0,i]*y[i] for i in range(3))

P.solve(solver='glpk')

print('x=', x)
print('y=', y)
print('Value:', P.value)