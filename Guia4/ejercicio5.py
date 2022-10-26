import numpy as np
import matplotlib.pyplot as plt

Nflights = 1000
time_arr = np.zeros(Nflights)
prob = np.zeros(Nflights)

for flight in range(Nflights):
  time = np.random.normal(300, 20)
  time_arr[flight] = time

  if time > 350:
    prob[flight] = 1.0

print('Tiempo promedio de vuelo: ', np.mean(time_arr))
print('Probabilidad de que el vuelo tarde mas de 350 minutos: ', np.sum(prob)/Nflights)
plt.hist(density=True,  x=time_arr, range=(250,500), bins=25)
plt.xlabel('Tiempo de vuelo (min)')
plt.ylabel('Probabilidad')
plt.show()