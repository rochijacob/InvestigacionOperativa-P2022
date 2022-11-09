import numpy as np

#Tiempo entre arribo - clientes nuevos
lambda_param = 3
#Tiempo de atencion - clientes atendidos
mu = 2

T = 24 #horas
dt = 1/T

n_sim = int(T/dt)

# Arrays de simulacion
n_personas = np.zeros(n_sim)
evento_arribo = [False]*n_sim #array de false
evento_servicio = [False]*n_sim

# Estado inicial del sistema
n_personas[0] = 0

for i in range(1, n_sim):

  prob_arribo = 1 - np.exp(-lambda_param*dt)
  x = np.random.uniform() #Nose bien que hace esta x (?)

  if x <= prob_arribo:
    #Si la probabilidad de arribo es mayor y la cantidad de personas ANTES es menor a 2
    evento_arribo[i] = True

  if 0 < n_personas[i-1]: #si hay mas de 0 personas tengo el evento "despacho"
    prob_servicio = 1 - np.exp(-mu*dt)
    x = np.random.uniform()

    if x <= prob_servicio:
      evento_servicio[i] = True

  #Mi ecuacion que me va a decir la cantidad de personas

  n_personas[i] = n_personas[i - 1] + 1*evento_arribo[i] - 1*evento_servicio[i]

# Post-procesamiento
server_ocupado = n_personas > 0
fraccion_server_ocupado = np.sum(server_ocupado)/n_sim

print("a) Clientes atendidos en promedio por hora: ", np.sum(evento_servicio)/T)
print("b) Probabilidad de no atender a ningun cliente: ", 1 - fraccion_server_ocupado)