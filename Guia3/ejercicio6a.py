from scipy import optimize
import numpy as np

#a)

def f(x):
  function = (x[0] - 2)**2 + (x[0] - 1)*(x[1] - 1) + (x[1] - 3)**2 #Defino mi funcion objetivo 

  return function

def const1(x): #Restriccion 1
  constA = x[1]-2*x[0]-2
  return constA

def const2(x): #Restriccion 2
  constB = x[0]**2+x[1]**2-8
  return constB

const3 = optimize.NonlinearConstraint(const1, lb=0, ub=0) 
const4 = optimize.NonlinearConstraint(const2, lb=-np.inf, ub=0) #hace que sea menor o igual a 0
constraints = (const3, const4)

#Otra forma de definir los constraints
# constraints=({'type':'eq','fun':c1},
#             {'type':'ineq','fun':c2})


xopt=[]
fopt= np.inf

N = 1000
for i in range(N):
    # La semilla se define de manera aleatoria
    x0 = np.random.rand(2)*100
    #Optimizo
    opt = optimize.minimize(f, x0 = x0, constraints = constraints)
    # Guarda la funcion optima. En la segunda validacion se fija que en cada iteracion para guardarla la funcion optima que arroja scipy sea menor a la ultima optima que guardamos
    if opt.success == True and opt.fun < fopt:
        fopt = opt.fun
        xopt = opt.x
        bestopt = opt
print("x0 =" + str(x0) + "\n" + 
      "opt.x =" + str(np.around(opt.x,2)) +"\n"+ 
      "opt.fun =" + str(np.around(opt.fun,2))) 
print(bestopt)