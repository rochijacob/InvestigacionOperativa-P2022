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

Npers = 100

#En que estado me voy
leave_partner = np.zeros(Npers)

#Cuanto tardo en llegar a eso
time = np.zeros(Npers)

for persona in range(Npers):
  # Array donde guardo todas mis posiciones
  positions = np.zeros((Nyears, 5))
  positions[0, :] = p0  # entro como junior

  left = False

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

    #Veo si se fue o no
    if not left and nueva_posicion[3] == 1.0 or nueva_posicion[4] == 1.0:
      left = True
      time[persona] = year

  #Veo si se fue como partner
  if nueva_posicion[4] == 1.0:
    leave_partner[persona] = 1.0

print('Probabilidad de irse como partner', np.sum(leave_partner)/Npers)
print('Media de irse: ', np.mean(time))


plt.plot(positions[:, 0], 'o',  label='junior')
plt.plot(positions[:, 1], 'o',  label='senior')
plt.plot(positions[:, 2], 'o', label='partner')
plt.plot(positions[:, 3], 'o',  label='NP')
plt.plot(positions[:, 4], 'o', label='P')
plt.legend()

plt.show()