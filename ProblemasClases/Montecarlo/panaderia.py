"""
Pierre’s Bakery bakes and sells french bread. Each morning, the bakery satisfies the demand for the day using freshly baked bread. Pierre’s can bake the bread only in batches of a dozen loaves each. Each loaf costs 25¢ to make. For simplicity, we assume that the total daily demand for bread also occurs in multiples of 12. Past data have shown that this demand ranges from 36 to 96 loaves per day. A loaf sells for 40¢, and any bread left over at the end of the day is sold to a charitable kitchen for a salvage price of 10¢/loaf. If demand exceeds supply, we assume that there is a lost-profit cost of 15¢/loaf (because of loss of goodwill, loss of customers to competitors, and so on). The bakery records show that the daily demand can be categorized into three types: high, average, and low. These demands occur with probabilities of .30, .45, and .25, respectively. The distribution of the demand by categories is given in Table 7. Pierre’s would like to determine the optimal number of loaves to bake each day to maximize profit (revenues + salvage revenues - cost of bread - cost of lost profits).
"""
import numpy as np
import matplotlib.pyplot as plt

coin = np.random.rand()

if coin < 0.3:
  print('High')
elif coin > 0.3 and coin < (0.3+0.45):
  print('Avg')
elif coin > (0.3+0.45):
  print("Low")

diferencia = []
avg_ganancia = np.zeros(6)
for i,supply in enumerate([36, 48, 60, 72, 84, 96]):
  N = 100

  ganancia = np.zeros(N) 
  for day in range(N): 
    tipo_demanda = np.random.choice(['High', 'Avg', 'Low'], p=[0.3, 0.45, 0.25])

    if tipo_demanda == 'High':
      p_dia = [0.05, 0.1, 0.25, 0.3, 0.2, 0.1]
    elif tipo_demanda == 'Avg':
      p_dia = [0.1, 0.2, 0.3, 0.25, 0.1, 0.05]
    elif tipo_demanda == 'Low':
      p_dia = [0.15, 0.25, 0.35, 0.15, 0.05, 0.05]

    demanda = np.random.choice([36, 48, 60, 72, 84, 96], p =p_dia)

    diferencia = demanda - supply

    if diferencia > 0:
        ganancia[day] = 40*demanda - 25*supply + 10*diferencia
    else: 
        ganancia[day] = 40*demanda - 25*supply - 15*abs(diferencia)
    
  avg_ganancia[i] = np.sum(ganancia)/N

print(avg_ganancia)

plt.plot([36, 48, 60, 72, 84, 96], avg_ganancia)
plt.xlabel('Cantidad de panes')
plt.ylabel('Ganancia promedio')
plt.show()