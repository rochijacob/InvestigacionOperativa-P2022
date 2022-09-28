import picos
import numpy as np

P = picos.Problem()

x = picos.IntegerVariable('x', 5, lower = 0) #¿Cuando uso interger variable?
y = picos.BinaryVariable('y', 5) #Mis hornos

#Matriz de Costos Fijos
cf = np.array([[100, 200, 100, 200, 400]]) #Matriz & Costo fijo expresado en miles

#Matriz de Costos Variables
cv = np.array([[5, 8, 7, 5, 2]])

#Matriz de restriccion a la produccion
prod = np.array([[400, 400, 400, 400, 400]])

gases = np.array([[60, 40, 20, 40, 100]])


#Funcion Objetivo
P.set_objective('min', cf*y + cv*x)


#Restricciones
#Cumplimiento con la demanda
P.add_constraint(sum(x) == 1000)
#capacidad maxima
P.add_constraint(x<=prod)
#No puede emitir mas de 50mil toneladas
P.add_constraint(60*x[0] + 40*x[1] + 20*x[2] + 40*x[3] + 100*x[4] <= 50000)
#Restriccion de hornos apagados/prendidos
P.add_list_of_constraints(x[i] <= prod[0,i]*y[i] for i in range(5))

P.solve(solver='glpk')

print('x=', x)
print('y=', y)
print('Value:', P.value)