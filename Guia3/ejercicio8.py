from scipy import optimize
import numpy as np

def f(x):
    f = x[0]*50 + x[1]*100
    return f
def c1(x):
    return 0.5*np.sqrt(x[0])+1.7*np.sqrt(x[1])
cons1= optimize.NonlinearConstraint(fun= c1, lb = 40 , ub =np.inf)
def c2(x):
    return 2*np.sqrt(x[0])+0.7*np.sqrt(x[1])
cons2= optimize.NonlinearConstraint(fun= c2, lb = 60 , ub =np.inf)

constraints = (cons1, cons2)
bounds = [(0, None), (0, None)]

xopt = []
fopt = np.inf

N = 25
for i in range(N):
    # La semilla se define de manera aleatoria
    x0 = np.random.rand(2)*100
    #Optimizo
    opt = optimize.minimize(f, x0 = x0, constraints = constraints, bounds = bounds)
    # Si el optimo computado tiene mejor valor optimo, me quedo con  ese
    if opt.success == True and opt.fun < fopt:
        fopt = opt.fun
        xopt = opt.x
        bestopt = opt

print("x0 =" + str(x0) + "\n" + 
      "opt.x =" + str(np.around(opt.x,2)) +"\n"+ 
      "opt.fun =" + str(np.around(opt.fun,2))) 
print(bestopt) 