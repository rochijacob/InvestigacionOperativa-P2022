# There six cities in Kilroy County. The county must determine where to build firestations. The county wants to build the minimum number of firestations needed to ensure that at least one firestation is within 15 minutes (driving time) of each city. The times (in minutes) required to drive between the cities in Kilroy County are shown in table 6. Formulate an IP that will tell Kilroy County how many firestations to build and where to build them.

import picos
import numpy as np

P = picos.Problem()

y = picos.BinaryVariable('y', 6)

t = np.array([[0, 10, 20, 30, 30, 20],
     [10, 0, 25, 35, 20, 10],
     [20, 25, 0, 15, 30, 20],
     [30, 35, 15, 0, 15, 25],
     [30, 20, 30, 15, 0, 14],
     [20, 10, 20, 25, 14, 0]])

t = picos.Constant('t', t, (6, 6))

P.set_objective('min', sum(y))

P.add_constraint(y[0] + y[1] >= 1) #Ya se que ciudades tienen a menos de 15 minutos
P.add_constraint(y[0] + y[1] + y[5] >= 1)
P.add_constraint(y[2] + y[3] >= 1)
P.add_constraint(y[2] + y[3] + y[4] >= 1)
P.add_constraint(y[3] + y[4] + y[5] >= 1)
P.add_constraint(y[1] + y[4] + y[5] >= 1)

P.solve()

print(y)
print(P.value)