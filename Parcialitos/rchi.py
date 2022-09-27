from scipy import optimize
import numpy as np

def f_obj(x):
    return 200*np.sqrt((5-x[0])**2+(10-x[1])**2)+150*np.sqrt((10-x[0])**2+(5-x[1])**2)+200*np.sqrt((0-x[0])**2+(12-x[1])**2)+300*np.sqrt((12-x[0])**2+(0-x[1])**2)

def constraint1(x):
    return 2*x[0]+x[1]-14

def constraint2(x):
    return -x[0]+x[1]-2

const = ({'type': 'ineq', 'fun': constraint1},
         {'type': 'ineq', 'fun': constraint2})

x_opt = []
f_opt = np.inf #establezco como funcion optima un valor muy grande

#Voy a buscar un minimo local, iterando en todos los N's de mi problena
N = 100 #Voy a realizar 100 iteraciones
for i in range(N):
    x0 = np.random.rand(2) #Genero un punto aleatorio en el espacio de busqueda
    opt = optimize.minimize(f_obj, x0, const)
    if opt.fun < f_opt:
        x_opt = opt.x
        f_opt = opt.fun

print('Funcion optimizacion devuelve: ', opt)