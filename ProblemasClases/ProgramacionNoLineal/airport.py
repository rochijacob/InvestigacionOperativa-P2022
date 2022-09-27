from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri

#Problema del aeropuerto
#Objetivo: minimizar la distancia entre los dos puntos

# Defino que L como un número que va a estar fijo
L = 1

# Defino la función objetivo a minimizar
def f(x):
  return np.sqrt((x[0] - L/2)**2 + x[1]**2) + np.sqrt((x[0] + L/2)**2 + x[1]**2) + np.sqrt(x[0]**2 + (x[1] + - np.sqrt(3)/2*L)**2)

# optimize.minimize necesita que ingresemos a mano un valor inicial
x0 = [0, 0]
# optimizo la funcion objetivo. Busco el valor optimo para la ubicación
# del aeropuerto
opt = optimize.minimize(fun = f, x0 = x0)

print(opt)
print('Poniendo opt.x[0] obtenemos: ', opt.x[0])
print('Poniendo opt.x[1] obtenemos: ', opt.x[1])


# Lo siguiente es solamente para realizar el grafico
x_vec = [0, -L/2, L/2, round(opt.x[0],3)]
y_vec = [np.sqrt(3) * L / 2, 0, 0, round(opt.x[1],3)]
leg_ = ['Ciudad 1', 'Ciudad 2', 'Ciudad 3', 'Aeropuerto: (%.2f, %.2f)'%(x_vec[3],y_vec[3])]

triangles = [[0, 1, 2]]
triang = tri.Triangulation(x_vec, y_vec, triangles)

for i in range(len(x_vec)):
  plt.scatter(x_vec[i], y_vec[i], label = leg_[i])

plt.triplot(triang, lw=1, zorder=0) # draw the outlines of the triangles

plt.xlabel('x')
plt.ylabel('y')
plt.title('Ubicación del aeropuerto y las ciudades')
plt.legend()
plt.tight_layout()
plt.show()
