"""
El datacenter de una empresa de cloud computing puede tomar tres niveles
distintos de demanda de operaciones día-a-día: baja demanda, media demanda
y alta demanda. Basándonos en los registros históricos se determina que:
● Cada vez que el datacenter está en baja demanda, existe una probabilidad de
0.3 de quedarse en demanda baja al día siguiente, 0.5 de pasar a demanda
media y 0.2 de pasar de alta demanda.
● Cada vez que el sistema está en demanda media existe un 0.2 de pasar a
demanda baja, 0.4 de quedarse en demanda media y 0.4 de pasar a demanda
alta.
● Por último, cada vez que el sistema está en demanda alta existe un 0.2 de
quedarse en demanda alta al día siguiente, 0.5 de pasar a demanda media y 0.3
de pasar a demanda baja.
Se supone que el sistema está gobernado por un proceso estocástico markoviano
donde solo el estado actual determina el estado en el tiempo t+1. Si hoy el datacenter
está en demanda baja, se solicita saber cuál es la probabilidad de que en 3 días el
datacenter se encuentre en demanda alta.
"""
import numpy as np
import matplotlib.pyplot as plt

# Matriz de transición
p1 = np.array([[0.3, 0.5, 0.2], [0.2, 0.4, 0.4], [0.2, 0.5, 0.3]])
Ndias = 1000
final = 3

p0 = np.array([1, 0, 0]) #Probabilidad inicial

dias = np.zeros(Ndias)
estados = np.zeros((Ndias, 3)) #Un vector de 0 s por dia del mes con dos estados posibles

#Prob de que en 3 dias este bajo

p2 = np.dot(p1, p1)

p3 = np.dot(p1, p2)

p4 = np.dot(p0, p3)

print(p4[2])
