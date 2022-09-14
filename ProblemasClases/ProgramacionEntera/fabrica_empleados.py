#Version entera
import picos
import numpy as np

P = picos.Problem()
X = picos.BinaryVariable('X', (4,4))

C = np.array([[14, 5, 8 ,7],
              [2, 12, 6, 5],
              [7, 8, 3, 9],
              [2, 4, 6, 10]])
C = picos.Constant('C', C)

P.set_objective('min', C|X)

# El empleado ii debe ir a solo una etapa
for ii in range(4):
  P.add_constraint(picos.sum(X[ii, :]) == 1)

# La etapa jj debe recibir solo un empleado
for jj in range(4):
  P.add_constraint(picos.sum(X[:, jj]) == 1)

P.solve(solver='glpk')
print(P)
print(X)
print(P.value)