#Programacion lineal
import numpy as np
from scipy import optimize

#Planteo una funcion objetivo - la empresa quiere minimizar la distancia dada esta funcion de distancia

def f_obj(x):
    #Tengo dos variables, una es mi coordenada y y la otra mi coordenada x
    fun = 200*np.sqrt((5-x[0])**2+(10-x[1])**2)+150*np.sqrt((10-x[0])**2+(5-x[1])**2)+200*np.sqrt((0-x[0])**2+(12-x[1])**2)+300*np.sqrt((12-x[0])**2+(0-x[1])**2)
    return fun

x_opt = []
f_opt = np.inf #establezco como funcion optima un valor muy grande

#Voy a buscar un minimo local, iterando en todos los N's de mi problena
N = 100 #Voy a realizar 100 iteraciones

for i in range(N):
    x0 = np.random.rand(2) #Genero un punto aleatorio en el espacio de busqueda
    opt = optimize.minimize(f_obj, x0)
    if opt.fun < f_opt:
        x_opt = opt.x
        fopt = opt.fun

print('Funcion optimizacion devuelve: ', opt)

print('El punto de ubicacion optimo es', x_opt)
print('La funcion optima es', fopt)







# print("x0 =" + str(x0) + "\n" + 
#       "opt.x =" + str(np.around(opt.x,2)) +"\n"+ 
#       "opt.fun =" + str(np.around(opt.fun,2))) 
# print(bestopt)

