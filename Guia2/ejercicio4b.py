import picos
import numpy as np

P = picos.Problem()
x = picos.RealVariable('x', (3,6), lower = 0) #Matriz de descision, le agrego una columna mas
c = np.array([[31,29,32,28,20, 150],
     [45,41,46,42,43, 200],
     [38,35,40,10000,10000, 300]])

c = picos.Constant('c', c)

P.set_objective('min', x|c)

d = [1000, 1500, 900] #3600
s = [400, 600, 400, 600, 1000] #3000 - el problema esta desbalanceado

#Sumo todas las columnas - La suma de la columna me tiene que dar la demanda
for jj in range(len(d)):
  P.add_constraint(picos.sum(x[jj,:])== d[jj])

#Sumo todas las filas - la suma de todas las filas me tiene que dar menor o igual a la oferta
for ii in range(len(s)):
  P.add_constraint(picos.sum(x[:,ii]) <= s[ii])


P.solve()
print(x)
print(P.value)