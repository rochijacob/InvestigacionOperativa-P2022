"""
The law firm of Mason and Burger employs three types of lawyers: junior lawyers, senior lawyers, and partners. During a given year, there is a .15 probability that a junior lawyer will be promoted to senior lawyer and a .05 probability that he or she will leave the firm. Also, there is a .20 probability that a senior lawyer will be promoted to partner and a .10 probability that he or she will leave the firm. There is a .05 probability that a partner will leave the firm. The firm never demotes a lawyer. There are many interesting questions the law firm might want to answer.

1) What is the probability that a newly hired junior lawyer will leave the firm before becoming a partner?

2) How long does a newly hired junior lawyer stay with the firm?
"""
import numpy as np
import matplotlib.pyplot as plt
# Matriz de transición
P1 = np.array([[0.80, 0.15, 0.00, 0.05, 0.00],
               [0.00, 0.70, 0.20, 0.10, 0.00],
               [0.00, 0.00, 0.95, 0.00, 0.05],
               [0.00, 0.00, 0.00, 1.00, 0.00],
               [0.00, 0.00, 0.00, 0.00, 1.00]])

# Arranco como junior
p0 = np.array([1, 0, 0, 0, 0])

# Canidad de años
Nyears = 20

# Array donde guardo todas mis posiciones
positions = np.zeros((Nyears, 5))
positions[0, :] = p0  # entro como junior

for year in range(Nyears-1):
  posicion_actual = positions[year, :]

  # Probabilidades de quedarse en la posición, ascender o irse
  pronostico = np.dot(posicion_actual, P1)

  # Armamos nueva posicion
  nuevo_indice = np.random.choice([0, 1, 2, 3, 4], p=pronostico)
  nueva_posicion = np.zeros(5)
  nueva_posicion[nuevo_indice] = 1.0

  # Guardamos nueva posicion
  positions[year+1, :] = nueva_posicion

plt.plot(positions[:, 0], 'o',  label='junior')
plt.plot(positions[:, 1], 'o',  label='senior')
plt.plot(positions[:, 2], 'o', label='partner')
plt.plot(positions[:, 3], 'o',  label='NP')
plt.plot(positions[:, 4], 'o', label='P')
plt.legend()

print(positions)

plt.show()