import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
#Definicion de la funcion objetivo

def obj_fn(x):
  ''' Ganancia obtenida por dolar invertido en cada territorio '''
  return -(5*(6*np.sqrt(x[0])) + 5*(4*np.sqrt(x[1]))) #Lo hago negativo para maximizar 

#Defino restriccion

def restriccion(x):
  return x[0] + x[1]
constraint = optimize.NonlinearConstraint(fun=restriccion, ub=100, lb=0)

lb = 0
ub = np.inf

bounds = [(lb, ub), (lb,ub)]

#Valores iniciales
fopt = -np.inf
xopt = []

#Semilla
N = 100
for ii in range(N):
  x0 = np.random.rand(2)*100 #Me va a devolver dos numeros aleatorios

  opt = optimize.minimize(fun=obj_fn, constraints=constraint, bounds=bounds, x0=x0)

  if opt.success and -opt.fun > fopt:
    fopt = -opt.fun #valor optimo obtenido por el metodo
    xopt = opt.x
    seed = x0

print(fopt, xopt, seed)