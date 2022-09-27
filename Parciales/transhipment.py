import picos
import numpy as np

P = picos.Problem()

x = picos.RealVariable('x', 10, lower=0)

c = np.array([15, 20, 20, 15, 10, 15, 20, 15, 20, 25])
c = picos.Constant('c', c, (1, 10))

P.set_objective('min', c*x)

# Restricciones de transporte
#No hay

# Restricciones de Oferta

P.add_constraint(x[0] + x[1] <= 200)
P.add_constraint(x[2] + x[3] <= 800)

#Restricciones de Demanda

P.add_constraint(x[4] + x[7] == 200)
P.add_constraint(x[5] + x[8] == 300)
P.add_constraint(x[6] + x[9] == 500)

#Restricciones de Almacenes

P.add_constraint(x[0] + x[2] == x[4] + x[5] + x[6])
P.add_constraint(x[1] + x[3] == x[7] + x[8] + x[9])


P.solve()

print('Transporte')
print(x)
print(P.value)