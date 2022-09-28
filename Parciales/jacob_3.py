from scipy import optimize
import numpy as np

def f(x):
    r = 2*x[0]**2 + x[1]**2 + 0.1*(x[0]+x[1])**2
    return r

def inversion(x):
    i = 5*x[0] + 3*x[1] - 10
    return i

cons = optimize.NonlinearConstraint(inversion,  lb=10, ub=np.inf)

x0 = [0, 0]
opt = optimize.minimize(f, x0, constraints=cons)

print(opt.x)
print('Ganancia', inversion(opt.x))
