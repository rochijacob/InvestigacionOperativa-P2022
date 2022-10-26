import numpy as np
import matplotlib.pyplot as plt

games = 1000
fichas = 0
ganados = 0

stats = []

for game in range(1, games + 1):
  dado1 = np.random.choice(range(1,5), 1)
  dado2 = np.random.choice(range(1,4), 1)
  suma = dado1 + dado2

  if suma > 3 or suma > 4 or suma > 5: 
    ganados += 1
    fichas += 1
  elif suma < 3 or suma < 4 or suma < 5:
    fichas -= 1

  stats += [ganados/game]  

print('% de partidas ganadas', ganados/games)
print('% de partidas perdidas', (1 - ganados/games))
print('Balance neto de ganancia', fichas)

plt.plot(stats, 'b', label='Ganados')
plt.show()