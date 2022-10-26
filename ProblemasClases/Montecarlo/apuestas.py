"""
Sea un juego con las siguientes reglas:

El juego consiste en tirar una moneda hasta que la diferencia entre el número de caras y el número de cecas sea igual a 3. Hay que poner $1 cada vez que si tira la moneda. Cuando el juego termina uno recibe $8. Vale la pena jugar?
"""
import numpy as np
import matplotlib.pyplot as plt


N_exps = 20000  # Cuantas veces juego
resultados = []
for trial in range(N_exps):
  dinero  = 0
  N_juego = 1000 # Numero máximo de jugadas permitidas
  caras   = 0
  cecas   = 0
  for tirada in range(N_juego):
  
    # Pago para tirar
    dinero -= 1
  
    # Tiro la moneda
    moneda = np.random.choice(['cara', 'ceca'], p=[0.5, 0.5])
  
    # Me fijo que salió
    if moneda == 'cara':
      caras += 1
    elif moneda == 'ceca':
      cecas += 1

    # Veo si el juego termino
    if abs(caras-cecas) == 3:
      dinero += 8
      break  # Esto rompe el for loop de la tirada
    
  # Guardo el resultado de cada juego
  resultados.append(dinero)

resultados = np.array(resultados)

#Plot

_ = plt.hist(resultados, density=True, bins=15)
print(sum(resultados>0)/N_exps)
print(np.mean(resultados))
plt.axvline(np.mean(resultados), color='r', ls='--')

plt.show()