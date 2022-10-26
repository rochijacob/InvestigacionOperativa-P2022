import numpy as np
import matplotlib.pyplot as plt

days = 100
supplys = np.arange(250, 360, 10)
supply_list = np.zeros(11)

for index, supply in enumerate(supplys):
  ganancia_arr = np.zeros(days)
  for day in range(days):
    demand = int(np.random.normal(300, 50))

    ganancia = 1.25*demand - 0.75*supply
    ganancia_arr[day] = ganancia
  
  supply_list[index] = np.mean(ganancia_arr)


plt.plot(supplys, supply_list)
plt.show()