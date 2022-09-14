import picos
import numpy as np

P = picos.Problem()

x = picos.RealVariable('x', (5, 6), lower=0, upper=1000)

c = np.array([[13, 10, 22, 29, 18, 0],
     [14, 13, 16, 21, 10000, 0],
     [3, 0, 1000, 11, 6, 0],
     [18, 9, 19, 23, 11, 0],
     [30, 24, 34, 36, 28, 0]])

c = picos.Constant('c', c)

P.set_objective('min', c|x)

s = [5, 6, 7, 4, 3]
d = [3, 5, 4, 5, 6, 2]

for jj in range(5):
    P.add_constraint(picos.sum(x[jj, :]) <= s[jj])

for ii in range(6):
  P.add_constraint(picos.sum(x[:, ii]) == d[ii])

P.solve(solver='glpk')

print(P.value)