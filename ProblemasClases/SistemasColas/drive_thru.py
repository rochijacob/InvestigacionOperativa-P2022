"""
Una media de 10 autos por hora llegan a un negocio de comidas rápidas con drive-thru. Se supone que la media de servicio por cada cliente es de 4 minutos y que la distribución del tiempo entre arribos y entre servicio es exponencial.

¿Cuál es la probabilidad que el servidor esté libre?
¿Cuál es la media de autos esperando en la fila?
¿Cuál es la media que un auto pasa en el negocio?
¿Cuántos clientes por hora son atendidos por el server?
"""

import numpy as np

lambda_param = 10 #autos/hs
mu = 15 #60/4

#Parametros de la simulacion
T = 100 #Mi periodo de tiempo
dt = 0.0001
n_sim = int(T/dt)

#Arrays de simulacion
n_personas = np.zeros(n_sim)
evento_arribo = [False]*n_sim
evento_servicio = [False]*n_sim

t = np.arange(0, T, dt)

#Estado inicial del sistema
n_personas[0] = 0 #Apenas arranca el estado es 0

#Simulacion del sistema
for i in range(1, n_sim):
  #Arribos con probabilidad exponencial

  prob_arribo = 1 - np.exp(-lambda_param*dt)
  x = np.random.uniform()

  if x <= prob_arribo:
    evento_arribo[i] = True

  #Servicio con probabilidad exponencial

  if 0 < n_personas[i-1]:
    prob_servicio = 1 - np.exp(-mu*dt)
    x = np.random.uniform()
    if x <= prob_servicio:
      evento_servicio[i] = True

  n_personas[i] = n_personas[i-1] + 1*evento_arribo[i] - 1*evento_servicio[i] #El estado anterior + si llego una persona - si se fue una persona

#Post-Prosecasmiento

server_ocupado = n_personas > 0
n_personas_cola = np.maximum(n_personas-1, 0)
promedio_personas = np.mean(n_personas)
promedio_personas_cola = np.mean(n_personas_cola)
fraccion_server_ocupado = np.sum(server_ocupado)/n_sim

print("1. Probabilidad server libre: ", 1 - fraccion_server_ocupado)
print("2. Media autos esperando en la fila: ", promedio_personas_cola)
print("3. Media de tiempo en el negocio: ", np.sum(n_personas)*dt/np.sum(evento_arribo))
print("4. Clientes atendidos en promedio por hora: ", np.sum(evento_servicio)/T)