import matplotlib.pyplot as plt
import picos

def funcion(BD):
    P = picos.Problem()
    x = picos.RealVariable('x',9, lower = 0)
    P.set_objective('max', x[0]+x[1])
    P.add_constraint(x[0]<=9)
    P.add_constraint(x[1]<=7)
    P.add_constraint(x[2]<BD)
    P.add_constraint(x[3]<=2)
    P.add_constraint(x[4]<=4)
    P.add_constraint(x[5]<=6)
    P.add_constraint(x[6]<=3)
    P.add_constraint(x[7]<=6)
    P.add_constraint(x[8]<=9)
    P.add_constraint(x[0]==x[2]+x[3])
    P.add_constraint(x[1]==x[4]+x[5])
    P.add_constraint(x[2]+x[4]==x[6]+x[7])
    P.add_constraint(x[3]+x[5]+x[6]==x[8])
    P.solve()
    return x, P.value

BD_arr = range(0,12)
fopt_arr = []
for BD in BD_arr:
    xopt, fopt = funcion(BD)
    fopt_arr.append(fopt)
    print('xopt=', xopt)
    print('fopt=', fopt)
    
plt.plot(BD_arr, fopt_arr)
plt.show()