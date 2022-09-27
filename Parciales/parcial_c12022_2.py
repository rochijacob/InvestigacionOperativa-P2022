import picos
import numpy as np

#Problema binario donde no tengo matriz de costos

P = picos.Problem()

#Defino mis variables
y = picos.BinaryVariable('y', (3,7))

#Defino mi funcion objetivo
P.set_objective('min', picos.sum(y))

#Defino mis restricciones

#Cada uno puede ir solo a 1 turno
for jj in range(7):
    P.add_constraint(picos.sum(y[:,jj]) <= 1)

# Todos los turnos deben tener al menos dos personas
for ii in range(3):
    P.add_constraint(picos.sum(y[ii,:]) >= 2)

#Deben estar, A, B, C o D
P.add_constraint(y[0, 0] + y[0, 1] + y[0, 2] + y[0,3] >= 1)
P.add_constraint(y[1, 0] + y[1, 1] + y[1, 2] + y[1,3] >= 1)
P.add_constraint(y[2, 0] + y[2, 1] + y[2, 2] + y[2,3] >= 1)

#A y B no pueden estar juntas
for ii in range(3):
    P.add_constraint(y[ii, 0] + y[ii, 1] <= 1)

#Si C y D no estan juntas, F no puede estar
#Restriccion de AND: cuando nescesito que dos o mas se cumplan las multiplico y divido por el numero de variables, y asi me aseguro que la suma si es mayor a 1 no la cumple

for ii in range(3):
    P.add_constraint(y[ii, 5] + ((y[ii, 2]+y[ii,3])/2) <= 1)

P.solve(solver='glpk')

print('Distribucion de los trabajadores')
print(y)
print('# de trabajadores que asigno')
print(P.value)