from scipy import optimize
import numpy as np

def f_obj(x):
    return -(x[0]*x[1])

def capital(x):
    return 4*x[0] + x[1]

cons = optimize.NonlinearConstraint(fun=capital, lb=0, ub=8)

opt = optimize.minimize(f_obj, [1,1], bounds=[(0, None), (0, None)], constraints=cons)

print(opt.x)