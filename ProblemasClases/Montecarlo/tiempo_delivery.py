"""
En una pizzeria, el pizzero tarda entre 10 y 20 minutos en preparar una pizza, mientras que el delivery tarda entre 20 y 40 minutos en llevar el pedido. Ambos distribuidos uniformemente. ¿Cuanto tarda en promedio un pedido en llegar al cliente? ¿Cómo es la distribución? ¿Cual es la probabilidad de que el pedido tarde más de 40 minutos en llegar?
"""

import numpy as np
import matplotlib.pyplot as plt

def min_max(nums, min, max):
    ":nums agarra numeros entre 0 y 1"

    out = nums*(max-min) + min
    return out

N = 10000
pizza = min_max(np.random.rand(N), 10, 20)
delivery = min_max(np.random.rand(N), 20, 40)
tiempo = pizza + delivery

print('Media: ', str(np.mean(tiempo)), 'Desviacion: ', str(np.std(tiempo)))
print(sum(tiempo>40)/N)

_ = plt.hist(tiempo, bins=100)

plt.show()