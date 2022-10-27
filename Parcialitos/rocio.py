import numpy as np
import matplotlib.pyplot as plt


transition_matrix = np.array([[0.8, 0.15, 0.05], [0.2, 0.6, 0.2], [0.1, 0.15, 0.75]])
initial_matrix = np.array([1, 0, 0])
proba_bien = np.zeros(50)
proba_regular = np.zeros(50)
proba_mal = np.zeros(50)

#Si juega muchos partidos


#Si pongo un numero alto voy planchando la probabildiad de que juege regular bien o mal en cualquier partido
for partido in range(50):
    initial_matrix = np.dot(initial_matrix, transition_matrix)

    proba_bien[partido] = initial_matrix[0]
    proba_regular[partido] = initial_matrix[1]
    proba_mal[partido] = initial_matrix[2]


print(initial_matrix)
print(proba_bien)

plt.plot(proba_bien)
plt.xlabel('Cantidad de partidos jugados')
plt.ylabel('Probabildiad de cada partido')
plt.plot(proba_mal)
plt.plot(proba_regular)
plt.show()


# Punto 2
print('-----Punto 2')


P1 = np.array([[0.8, 0.1, 0.05, 0.05], [0.15, 0.06, 0.15, 0.1], [0.05, 0.1, 0.75, 0.1], [0, 0, 0, 1]])

# Arranco jugando bien
p0 = np.array([1, 0, 0, 0])

# Canidad de partidos
Nmatches = 10

# Array donde guardo todos mis resultados
partidos = np.zeros((Nmatches, 4))
partidos[0, :] = p0  # juego bien
seva = 0


for match in range(Nmatches-1):
  ultimo_partido = partidos[match, :]
  #print('Ultimo partido', ultimo_partido)

  pronostico = np.dot(ultimo_partido, P1) #Aca tengo que multiplicar las probabildiades, nose porque se me mantiene constante
  #print('pronostico', pronostico)
  
  
  #Elijo entre mis probabilidades
  nuevo_indice = np.random.choice([0, 1, 2, 3], p=pronostico)
  nuevo_partido = np.zeros(4)
  nuevo_partido[nuevo_indice] = 1.0

  if(partidos[match-1][3] == 1):
    seva += 1

  #print('nuevo partido', nuevo_partido)
  partidos[match+1, :] = nuevo_partido
  #print('upadted',partidos)

print('En promedio debe jugar: ')
print('En promedio deberia jugar entre 7 y 8 partidos, esto lo vi achicando el numero')
print('no me da el tiempo pero el seva deberia ser un array de 0s y a esos yo les saco la media, y asi obtengo cuantos partidos aproximadamente tarda en irse')


