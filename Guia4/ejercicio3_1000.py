import numpy as np
import matplotlib.pyplot as plt

Nsimulations = 1000
intervals = np.arange(0, 10, 2)
results = np.zeros(Nsimulations)

for simulation in range(Nsimulations):
  step1 = np.random.uniform(0, 2)
  step2 = np.random.exponential(1)
  step3 = np.random.triangular(0, 3, 4)

  results[simulation] = step1 + step2 + step3

print('Promedio: ', np.mean(results))

print('Desviacion estandar: ', np.std(results) )
plt.hist(results, bins=intervals, density=True)