import picos
import numpy as np

P = picos.Problem()

x = picos.BinaryVariable('x', (3,4))

rates = picos.Constant('rates', [20, 30, 30, 40])

c = np.array([
              [820, 810, 840, 960],
              [800, 870, 1e4, 920],
              [740, 900, 810, 840]
            ])

c = picos.Constant('c', c)

P.add_list_of_constraints([picos.sum(x[:,j]) == 1 for j in range(4)])
P.add_constraint(picos.sum(x[0, :]) <= 2)
P.add_constraint(picos.sum(x[1, :]) <= 2)
P.add_constraint(picos.sum(x[2, :]) == 1)

P.add_constraint(picos.sum(x[0, :] * rates) <= 75)
P.add_constraint(picos.sum(x[1, :] * rates) <= 75)
P.add_constraint(picos.sum(x[2, :] * rates) <= 45)

P.add_constraint(x[1,2] == 0)

P.set_objective('min', picos.sum(c^x))

print(P)

P.solve(solver = 'glpk')
print(x.value)