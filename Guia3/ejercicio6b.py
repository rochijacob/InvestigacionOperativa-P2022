from scipy import optimize
import numpy as np

#b)
def f(x):
  func = (1/5)*(x[0]-1)**6 - (5/4)*(x[0]-1)**4+2*(x[0]-1)**2+(1/4)*(x[1]-3)**6 - (5/4)*(x[1]-3)**4+2*(x[1]-3)**2
  return func



xopt=[]
fopt= np.inf

N = 1000
for i in range(N):
    # La semilla se define de manera aleatoria
    x0 = np.random.rand(2)*100
    #Optimizo
    opt = optimize.minimize(fun=f, x0 = x0)
    # Si el optimo computado tiene mejor valor optimo, me quedo con ese
    if opt.success == True and opt.fun < fopt:
        fopt = opt.fun
        xopt = opt.x
        bestopt = opt
print("x0 =" + str(x0) + " \n" + 
      "opt.x =" + str(np.around(opt.x,2)) +"\n"+ 
      "opt.fun =" + str(np.around(opt.fun,2))) 
print(bestopt)