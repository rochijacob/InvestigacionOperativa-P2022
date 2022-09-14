import picos
import numpy as np

P = picos.Problem()

x_rt = picos.RealVariable('x_rt', 3, lower=0)
x_ot = picos.RealVariable('x_ot', 3, lower=0)
x_d = picos.RealVariable('x_d', 3,lower=0)

P.set_objective('min', 31*x_rt[0] + 38*x_ot[0] + 3*x_d[0] + 31*x_rt[1] + 38*x_ot[1] + 3*x_d[1] + 36*x_rt[2] + 44*x_ot[2] + 3*x_d[2] )

rt = [10, 8, 10]
ot = [3, 2, 3]

P.add_constraint(x_rt[0]<=10)
P.add_constraint(x_rt[1]<=8)
P.add_constraint(x_rt[2]<=10)
P.add_constraint(x_ot[0]<=3)
P.add_constraint(x_ot[1]<=2)
P.add_constraint(x_ot[2]<=3)
P.add_constraint(x_rt[0]+x_ot[0]==8+x_d[0])
P.add_constraint(x_rt[1]+x_ot[1]+x_d[0]==10+x_d[1])
P.add_constraint(x_rt[2]+x_ot[2]+x_d[1]==16+x_d[2])

# for ii in range(len(rt)):
#   P.add_constraint(x_rt[ii] <= rt[ii])

# for jj in range(len(ot)):
#   P.add_constraint(x_ot[jj] <= ot[jj])

# p = [8, 10, 16]

# for hh in range(3):
#   P.add_constraint(x_rt[hh] + x_ot[hh] + x_d[hh] == p[hh] + x_d[hh])


P.solve()

print('Produccion Regular Time: \n', x_rt)
print('Produccion Over Time: \n', x_ot)
print('Almacenaje: \n', x_d)
print(P.value)