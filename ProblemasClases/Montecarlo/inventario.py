"""
Un supermercado recibe 1000 paquetes de yerba por semana. La demanda de yerba sigue una distribución normal con un promedio de 200 paquetes por día y una desviación estándar de 10 paquetes.

¿Cómo podemos simular este problem?
"""
import numpy as np
import matplotlib.pyplot as plt

W = 1000
acc = 0
acc_week = []

for week in range(W):
  supply = 1000
   #Cuantas veces llegue al final de la semana
  for day in range(5):
    demand = int(np.random.normal(200, 10))

    supply = supply - demand
    if(supply < 0):
      supply = 0

  #Termine la semana con paquetes o no?
  if supply == 0:
    acc += 1

  #Como cambia la estadistica semana a semana
  if week>0:
    acc_week.append(acc/(week +1))
  
print(acc/W)

plt.plot(acc_week)
plt.axhline(acc/W, ls='--')

plt.show()