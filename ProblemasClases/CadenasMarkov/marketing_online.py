"""
En el equipo de marketing online de una startup de la industria de internet tenemos una user-base de 2000 clientes con seguimiento en el mes 0 y el mes 1. Analizando las estadísticas de actividad, clicks, número de operaciones, tiempo utilizado, etc... se puede separar a los clientes en 9 grupos distintos, con una fuerta dependecia de dos de estas features. Utilizando las métricas mencionadas categorizamos a los clientes en 9 grupos para realizar marketing de precisión. Conociendo la transición de clientes entre el mes 0 y el mes 1 queremos estimar el número de clientes en cada categoría luego de 20 meses.
"""

import sklearn
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generamos un dataset X0 que tendra 2 variables a considerar y 2000 clientes para el mes 0
x0, y0 = make_blobs(n_samples=5000, centers=5, n_features=2, random_state=10, cluster_std = 2.3, center_box=(10,30))

# Generamos un dataset X1 que tendra 2 variables a considerar y 2000 clientes para el mes 1
x1, y1 = make_blobs(n_samples=5000, centers=5, n_features=2, random_state=10, cluster_std = 3, center_box=(12,29))

# Armo clasificador
num_estados = 9
classifier = KMeans(n_clusters=num_estados)
classifier.fit(x0)

# Armo estados para el mes 0 y mes 1
states0 = classifier.predict(x0)
states1 = classifier.predict(x1)

print(states0)


# Grafico del primer
plt.figure()
for ii in range(num_estados):
  plt.plot(x0[states0==ii, 0], x0[states0==ii, 1], '.')
plt.xlabel('Cantidad de visitas')
plt.ylabel('# de conversiones')
plt.title('Agrupamiento de usuarios en el primer mes')

# Grafico del segundo mes
plt.figure()
for ii in range(num_estados):
  plt.plot(x1[states1==ii, 0], x1[states1==ii, 1], '.')
plt.xlabel('Cantidad de visitas')
plt.ylabel('# de conversiones')
plt.title('Agrupamiento de usuarios en el segundo mes')

plt.show()

# Inicializo la matriz
P1 = np.zeros((num_estados, num_estados))

# Estimo las probabilidades de transición empíricamente
for ii in range(num_estados):
  for jj in range(num_estados):
    P1[ii, jj] = np.sum(states1[states0 == ii] == jj)/np.sum(states0 == ii)

plt.figure(figsize=(10, 6))
sns.heatmap(P1, annot=True)
sns.set_context('talk', font_scale=0.7)
plt.xlabel('Estado destino')
plt.xlabel('Estado origen')
plt.title("Matriz de Transición de 1 paso")

plt.show()

#Largo plazo

num_meses = 200

estados = np.zeros((num_meses, num_estados))
inicial = np.array([np.sum(states0 == ii)/5000 for ii in range(num_estados)])
estados[0, :] = inicial

# Matriz identidad para el paso 0
Pm = np.eye(num_estados)

for ii in range(num_meses-1):
  # Actualizo la matriz de transición
  Pm = np.dot(P1, Pm)

  # Pronostico el nuevo estado
  estados[ii+1, :] = np.dot(inicial, Pm)

sns.set_context(context='talk', font_scale=0.8)
plt.figure(figsize=(10,10))
meses = np.arange(num_meses)
for ii in range(num_estados):
  plt.plot(meses, estados[:, ii], '-o', label=f'grupo {ii+1}')
plt.xlabel('mes')
plt.ylabel('Fraccion de usuarios en cada grupo')
plt.legend() 

plt.show()