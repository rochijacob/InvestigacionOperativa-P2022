"""
En un centro de testeo de COVID arriban pacientes a una tasa media lambda = 50 pacientes/hora. Por cuestiones operativas cada vez que se acumulan 20 pacientes esperando se los hace pasar todos juntos para ser testeados. Si el tiempo entre arribos de pacientes se rige bajo una distribución de probabilidad exponencial, determinar luego de 500 experimentos independientes en cuanto tiempo total arribaran los primeros 20 pacientes.
"""
import numpy as np
import matplotlib.pyplot as plt

lambda_param = 50

#¿Cuantas personas llegan en una hora?

resultados = []

for experimento in range(1000):
  tiempo_total = 0
  num_arribos = 0

  while tiempo_total < 1.0:
    t_arribos = np.random.exponential(1/lambda_param)
    tiempo_total += t_arribos

    num_arribos += 1

  resultados.append(num_arribos)

print('Cantidad de personas que llegan en 1h:', np.mean(resultados))

#¿Cuanto tardan en llegar 20 personas?

tiempo_total = 0
num_arribos = 0

while num_arribos < 20:
    t_arribos = np.random.exponential(1/lambda_param)
    tiempo_total += t_arribos

    num_arribos += 1

print(f'Tiempo total en el que llegan {num_arribos} personas: ', tiempo_total)


#Para muchos experimentos 

cant_exps = 1000
num_personas = 20
experimentos = np.zeros((cant_exps, num_personas))

for trial in range(cant_exps):
  tiempo_total = 0
  
  for persona in range(20):
    t_arribo = np.random.exponential(1/lambda_param)
    tiempo_total += t_arribo
    experimentos[trial, persona] = t_arribo

tiempo_total_exp = np.sum(experimentos, axis=1)
tiempo_promedio = np.mean(tiempo_total_exp)
print('Tiempo promedio realizando un montecarlo: ', tiempo_promedio)

_ = plt.hist(tiempo_total_exp)
plt.show()

tiempo_acumulado = np.cumsum(experimentos, axis=1)
print('Experimentos: ', experimentos[0, :])
print('Acumulado: ', tiempo_acumulado[0, :])

# tiempos_espera = tiempo_total_exp - tiempo_acumulado
tiempos_espera = np.zeros((cant_exps, num_personas))
for trial in range(cant_exps):
  tiempos_espera[trial, :] = tiempo_total_exp[trial] - tiempo_acumulado[trial, :]

# print(tiempo_total_exp[0] - tiempo_acumulado[0, :])

espera_promedio_por_exp = np.mean(tiempo_acumulado, axis=1)
espera_promedio = np.mean(espera_promedio_por_exp)
print('Espera promedio', espera_promedio)