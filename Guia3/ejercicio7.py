from scipy import optimize
import numpy as np


def f2(x):
    fun = 200*np.sqrt((5-x[0])**2+(10-x[1])**2)+150*np.sqrt((10-x[0])**2+(5-x[1])**2)+200*np.sqrt((0-x[0])**2+(12-x[1])**2)+300*np.sqrt((12-x[0])**2+(0-x[1])**2)
    return fun


xopt = []
fopt = np.inf
N = 100

for i in range(N):
     # La semilla se define de manera aleatoria
    x0 = np.random.rand(2)*100
    # Optimizo
    opt = optimize.minimize(f2, x0)
    # Si el optimo computado tiene mejor valor optimo, me quedo con  ese
    if opt.success == True and opt.fun < fopt:
        fopt = opt.fun
        xopt = opt.x
        bestopt = opt
 
print("x0 =" + str(x0) + "\n" + 
      "opt.x =" + str(np.around(opt.x,2)) +"\n"+ 
      "opt.fun =" + str(np.around(opt.fun,2))) 
print(bestopt)