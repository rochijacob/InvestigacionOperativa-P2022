"""
PRECIO Y PUBLICIDAD

La cantidad vendida de un producto dependen del precio de venta y de la cantidad de publicidad online de acuerdo a la siguiente formula $q=1000*\frac{\sqrt{a}}{p^2}$, donde q es la cantidad total vendida, p es el precio de venta unitario y a son los segundos de publicidad online. El costo unitario de produccion del producto es de \$1 por unidad y el costo de cada segundo de publicidad es de \$0.1. La empresa tiene \$100000 en capital total para cubrir los costos de produccion y de publicidad online. **Asumiendo que va  aproducir exactamente la cantidad de unidades que va a vender (es decir, no produce mas de lo nescesario)** Cual es la estrategia de precio y publicidad optima si se quiere maximizar sus ganancias, dadas las limitaciones de capital?

NOTA: Recordar que en Python la funcion p^2 se puede expresar como p**2 y $\sqrt{a}$ como a**(0.5)
"""
from scipy import optimize
import numpy as np

#x[0]: a
#x[1]: p

def obj_function(x):
  beneficio = 1000*((x[1]**(0.5))/(x[0]**2))*x[0]
  costo = x[0] + 0.1*x[1] 
  f = -(beneficio - costo)
  return f

def costo(x):
    return x[0] + 0.1*x[1]

cons = optimize.NonlinearConstraint(fun=costo, lb=0, ub=100000)

xopt = []
fopt = np.inf

N = 1000
for i in range(N):
  x0 = np.random.rand(2)*100
  opt = optimize.minimize(fun=obj_function, x0=x0, constraints=cons)

  if opt.success == True and opt.fun < fopt:
    fopt = opt.fun
    xopt = opt.x

print(fopt, xopt)