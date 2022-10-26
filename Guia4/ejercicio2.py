import numpy as np
import matplotlib.pyplot as plt


Nlights = 1000
results = np.zeros(Nlights)
prob_evolution = np.zeros(Nlights)

for light in range(1, Nlights):
  #cada semaforo rojo se reinicia
  red_light = np.random.choice([0, 1, 2, 3, 4, 5], p=[0.1, 0.13, 0.21, 0.23, 0.2, 0.13])
  results[light] = red_light


print('Mean: ', np.mean(results))

plt.hist(results, 5)
plt.show()
