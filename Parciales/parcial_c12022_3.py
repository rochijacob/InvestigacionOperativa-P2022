from scipy import optimize
import numpy as np

#Funcion NoLinear Maximizacion

#x[0]: mi precio
#x[1]: mi cantidad gastada en publicidad

def f_obj(x):
    demanda = x[0]*(5*np.sqrt(x[0]) - x[0]**2 + (2*(x[1]**2) - x[1]**3))
    publicidad = x[1]
    fun = - (demanda - publicidad)
    return fun

bounds = [(0, np.inf), (0, 5)]

xopt = []
fopt = np.inf

N = 1000
for i in range(N):

    x0 = np.random.rand(2)
    opt = optimize.minimize(f_obj, x0, bounds=bounds)
    if opt.fun < fopt:
        xopt = opt.x
        fopt = opt.fun

print('Funcion optimizacion devuelve: ', xopt, fopt)


# #OPEN PYTHON FILE
# py = open('../Parcialitos/parcialito_c1.py', 'r')
# print(py.read())