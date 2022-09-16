import picos
import numpy as np

P = picos.Problem()

y = picos.BinaryVariable('y', (2,4) ) #Tiene 8 pq hay 8 posibles combinaciones

t = np.array([[4.5, 7.8, 3.6, 2.9],[ 4.9, 7.2, 4.3, 3.1]]) # el tiempo que en este caso es mi costo

t = picos.Constant('t', t)

P.set_objective('min', t|y) # transpongo la matiz para que sea multiplicable

## Restricciones de jugadores
for ii in range(2):
  P.add_constraint(picos.sum(y[ii, :]) == 2)

#Restricciones binarias

for jj in range(4):
  P.add_constraint(picos.sum(y[:, jj]) == 1)


P.solve(solver='glpk')

print('y= \n', y)
print('El tiempo total minimo es: ', round(P.value) )