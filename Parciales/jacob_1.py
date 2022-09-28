import picos
import numpy as np

#Flujo maximo

P = picos.Problem()

x = picos.BinaryVariable('x', 13)

c = np.array([10, 11, 14, 12, 16, 16, 11, 12, 20, 16, 16, 20, 10])
t = np.array([0.7, 1.8, 0.3, 1.5, 1.5, 1.5, 0.3, 0.7, 0.1, 0.6, 0.9, 0.1, 0.7])

t = picos.Constant('c', t, (13, 1))

P.set_objective('min', t|x)


P.add_constraint(x[0] == x[2] + x[3])
P.add_constraint(x[1] == x[4] + x[5])
P.add_constraint(x[2] == x[6] + x[7])
P.add_constraint(x[3] + x[6] + x[4] == x[8] + x[9])
P.add_constraint(x[5] == x[10])
P.add_constraint(x[7] + x[8] == x[11])
P.add_constraint(x[9] + x[10] == x[12])

#Lo que sale tiene que ser igual a lo que entra
P.add_constraint(x[0] + x[1] == x[11] + x[12])

P.add_constraint(x[0] + x[1] == 1)

P.solve()

print(P.value)
print('Camino que sigue')
camino = []
for index, arrow in enumerate(x):
    if round(arrow) == 1:
        camino.append(index + 1)
print('Va a seguir el camino: ', camino)
print('Costo por peaje', c|x)