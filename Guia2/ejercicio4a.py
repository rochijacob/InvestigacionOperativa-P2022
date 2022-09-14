import picos
import numpy as np
#A - Lo resuelvo sin el sumidero

P = picos.Problem()
x = picos.RealVariable('x', (3,5), lower = 0)
c = np.array([[31,29,32,28,20],
     [45,41,46,42,43],
     [38,35,40,10000,10000]])

P.set_objective('min', c|x)

d = [600, 1000, 800]
s = [400, 600, 400, 600, 1000]

for jj in range(3):
  P.add_constraint(picos.sum(x[jj,:])== d[jj])

for ii in range(5):
  P.add_constraint(picos.sum(x[:,ii])<= s[ii])


P.solve()
print(x)
print(P.value)

#B - Lo resuelvo con sumidero

P = picos.Problem()
x = picos.RealVariable('x', (4,5), lower = 0)
c = np.array([[31,29,32,28,20],
     [45,41,46,42,43],
     [38,35,40,10000,10000],
     [0, 0, 0, 0, 0]])

P.set_objective('min', c|x)

d = [600, 1000, 800, 600]
s = [400, 600, 400, 600, 1000]

for jj in range(4):
  P.add_constraint(picos.sum(x[jj,:])== d[jj])

for ii in range(5):
  P.add_constraint(picos.sum(x[:,ii])<= s[ii])


P.solve()
print(x)
print(P.value)