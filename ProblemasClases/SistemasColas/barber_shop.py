"""
Una peluquería tiene un solo empleado y 10 asientos disponibles en el sistema. 
El tiempo entre arribos se distribuye exponencialmente con una media de 20 clientes por hora.
Los clientes que encuentran la peluquería llena no entran. 
La media de tiempo de servicio es de 12 minutos y se distribuye exponencialmente.
"""

import numpy as np

# Parametros del sistema
lam = 20  # autos/hs
mu = 5   # autos/hs

# Parametros de la simulacion
T = 1000   # hs
dt = 0.0001 # hs 
n_sim = int(T/dt)

# Arrays de simulacion
n_personas = np.zeros(n_sim)
evento_arribo = [False]*n_sim
evento_servicio = [False]*n_sim

# Estado inicial del sistema
n_personas[0] = 0

# Evolucion del sistema
for i in range(1, n_sim):
    # Arribos con probabilidad exponencial
    prob_arribo = 1 - np.exp(-lam*dt)
    x = np.random.uniform()
    if x <= prob_arribo and n_personas[i-1]<10:
        evento_arribo[i] = True

    # Servicio con probabilidad exponencial
    if 0 < n_personas[i-1]:
        prob_servicio = 1 - np.exp(-mu*dt)
        x = np.random.uniform()
        if x <= prob_servicio:
            evento_servicio[i] = True
    
    n_personas[i] = n_personas[i-1] + 1 * evento_arribo[i] - 1 * evento_servicio[i]

# Post-procesamiento
server_ocupado = n_personas > 0
n_personas_cola = np.maximum(n_personas-1, 0)
promedio_personas = np.mean(n_personas)
promedio_personas_cola = np.mean(n_personas_cola)
fraccion_server_ocupado = np.sum(server_ocupado)/n_sim

print("1. Probabilidad de silla libre: ", 1 - fraccion_server_ocupado)
print("2. Media clientes esperando en la fila: ", promedio_personas_cola)
print("3. Media de tiempo en el negocio: ", np.sum(n_personas)*dt/np.sum(evento_arribo))
print("4. Clientes atendidos en promedio por hora: ", np.sum(evento_servicio)/T)