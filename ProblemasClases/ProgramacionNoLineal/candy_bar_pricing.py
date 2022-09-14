from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt


# Demanda en funcion del precio de la unidad (x) para la region 1
def demanda_region1(x):
  if x <= 1.3:
    return (32 - 35) / (1.3 - 1.1) * (x - 1.1) + 35
  else:
    return (22 - 32) / (1.5 - 1.3) * (x - 1.3) + 32

# Demanda en funcion del precio de la unidad (x) para la region 2
def demanda_region2(x):
  if x <= 1.3:
    return (27 - 32) / (1.3 - 1.1) * (x - 1.1) + 32
  else:
    return (16 - 27) / (1.5 - 1.3) * (x - 1.3) + 27

# Demanda en funcion del precio de la unidad (x) para la region 3
def demanda_region3(x):
  if x <= 1.3:
    return (17 - 24) / (1.3 - 1.1) * (x - 1.1) + 24
  else:
    return (9 - 17) / (1.5 - 1.3) * (x - 1.3) + 17

# Funcion objetivo, tengo que poner un menos porque busco maximizar
# usando la funcion minimizar y: max(f(x)) = - min(- f(x))
def f(x):
  return -x * (demanda_region1(x) + demanda_region2(x) + demanda_region3(x))

opt = optimize.minimize(fun = f, x0 = 0, bounds = [(1.1, 1.5)])

print(opt)
print('Valor Óptimo: ', -opt.fun[0])
print('Punto Óptimo: ', opt.x[0])

# Lo siguiente es solamente para realizar el grafico
x_plot = np.linspace(1.1, 1.5, 100)
f_plot = np.zeros(len(x_plot))
for i in range(len(x_plot)):
  f_plot[i] = -f(x_plot[i])
plt.plot(x_plot, f_plot)
plt.scatter(round(opt.x[0],3), -f(round(opt.x[0],3)),
            label = 'Punto Óptimo: {}\nValor Óptimo: {}'.format(round(opt.x[0],3), (round(-opt.fun[0],3))),
            color = 'r')
plt.vlines(round(opt.x[0],3), 70, 99, linestyles = 'dashed', color = 'r')

plt.xlabel('precio del producto')
plt.ylabel('Facturación')
plt.title('Facturación esperada según el precio asignado al producto')
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()
