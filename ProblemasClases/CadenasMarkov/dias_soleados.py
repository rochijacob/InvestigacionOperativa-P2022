"""
En un pueblo, al 90% de los días soleados le siguen días soleados, y al 80% de los días nublados le siguen días nublados. Con esta información modelar el clima del pueblo como una cadena de Markov.

Si el dia de hoy el clima es soleado, cual es la probabilidad que en 3 dias el clima sea soleado?

Cual es la probabilidad de tener dias soleados en el largo plazo?
"""
import numpy as np
import matplotlib.pyplot as plt

#Me hago una matriz
p1 = ([[0.9, 0.1], [0.2, 0.8]])

#Calculo la probabilidad de que en 3 dias el clima sea soleado
p2 = np.dot(p1, p1)

p3 = np.dot(p1, p2)

p0 = np.array([1, 0]) #Probabilidad inicial

p4 = np.dot(p0, p3)

print(p4)

#Calculo la probabilidad de que en el largo plazo el clima sea soleado

Ndias = 30

matrix = np.array([[1, 0], [0, 1]])

estados = np.zeros((Ndias, 2)) #Un vector de 0 s por dia del mes con dos estados posibles

for day in range(Ndias):
    matrix = np.dot(p1, matrix)

    estados[day, :] = np.dot(p0, matrix)


plt.plot(estados[:, 0], label = "Soleado")
plt.plot(estados[:, 1], label = "Nublado")

plt.show()

