import numpy as np
import matplotlib.pyplot as plt

#Punto i

days = 100
ganancia_arr = np.zeros(days)
supply = 350

for day in range(days):
  demand = round(np.random.normal(300, 50))

  if demand > supply:
    demand = supply

  ganancia = 1.25*demand - 0.75*supply
  ganancia_arr[day] = ganancia
  
print('Ganancia promedio por dia: ', np.mean(ganancia_arr))