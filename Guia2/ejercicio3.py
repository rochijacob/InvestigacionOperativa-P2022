import picos
import numpy as np


#Resuelvo el problema des-balanceado

P = picos.Problem()

x = picos.RealVariable('x', 6, lower=0)

c = np.array([400, 490, 460, 600, 530, 560])

a1 = np.array([[1, 1, 1, 0, 0, 0],
              [0, 0, 0, 1, 1, 1]]
              )
a2 = np.array([[1, 0, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 0],
              [0, 0, 1, 0, 0, 1]])

c = picos.Constant('c', c)
a1 = picos.Constant('a1', a1)
a2 = picos.Constant('a2', a2)

P.set_objective('min', c.T*x)

s = np.array([18, 14])
d = np.array([10, 5, 10])

s = picos.Constant('s', s, (2, 1))
d = picos.Constant('d', d, (3, 1))

print(x)

P.add_constraint(a1*x <= s)
P.add_constraint(a2*x == d)


P.solve(solver='glpk')

print(P.value)