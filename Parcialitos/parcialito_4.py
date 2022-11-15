"""
En una discoteca, el personal de la puerta no permite ingresar a nadie hasta que se forme una fila de al menos 50 personas afuera. Al lugar llegan en promedio 60 personas por hora, pero no todas deciden quedarse a esperar siempre. Si la fila tiene entre 0 y 24 personas una persona que llega se va a quedar a esperar incondicionalmente, si la fila tiene entre 25 y 40 personas, una persona que llega tiene 0.75 probabilidades de
quedarse a esperar, mientras que si la fila tiene más de 40 personas, una persona tiene solo 0.5 probabilidades de quedarse a esperar. ¿Cuánto tarda, en promedio, en formarse una fila de 50 personas?
"""
import numpy as np

lam = 60


# Parametros de la simulacion
T = 100  # hs
dt = 1/T # hs 

n_sim = int(T/dt)

# Arrays de simulacion
n_personas = np.zeros(n_sim)
evento_arribo = [False]*n_sim

# Estado inicial del sistema
n_personas[0] = 0
tiempo = np.zeros(n_sim)

# Evolucion del sistema
for i in range(1, n_sim):
    tiempo[i] = i*dt
    # Arribos con probabilidad exponencial
    prob_arribo = 1 - np.exp(-lam*dt)
    x = np.random.uniform()

    if x <= prob_arribo:
        if n_personas[i-1] <= 24:
            evento_arribo[i] = True
        elif n_personas[i-1]>24 and n_personas[i-1]<40:
            se_queda = np.random.choice([True, False], p=[0.75, 0.25])
            if se_queda:
                evento_arribo[i] = True
        elif n_personas[i-1]>=40 and n_personas[i-1]<50:
            se_queda = np.random.choice([True, False], p=[0.5, 0.5])
            if se_queda:
                evento_arribo[i] = True
    
    n_personas[i] = n_personas[i-1] + 1 * evento_arribo[i]

llego_50 = n_personas < 50
donde_llego = np.sum(llego_50)
print(donde_llego)
print('Tiempo aproximado donde llega a 50 personas: ', tiempo[donde_llego])





