import picos
import numpy as np
P = picos.Problem()

y = picos.BinaryVariable('y', 7)

#manejo de balon
bh= np.array([[3,2,2,1,3,3,3]])
#tiro
s= np.array([[3,1,3,3,3,1,2]])
#rebote
r= np.array([[1,3,2,3,3,2,2]])
#defensa
d= np.array([3,2,2,1,3,3,1])

d = picos.Constant('d', d)

P.set_objective('max', y|d)

#Tengo que tener 5 jugadores
P.add_constraint(sum(y)==5)

#Por lo menos 4 jugadores juegan en Guard (G)
P.add_constraint(y[0]+y[2]+y[4]+y[6] >= 4)
#Por lo menos 2 jugadores juegan en forward (F)
P.add_constraint(y[2]+y[3]+y[4]+y[5]+y[6] >= 2)
#Por lo menos 1 jugador juega en center (C)
P.add_constraint(y[1]+y[3]+y[5] >= 1)

# Promedio de 2 en ballhandling, shooting y rebound
m = [bh, s, r]

P.add_list_of_constraints(sum(m[i]*y)/5 >= 2 for i in range(len(m)) )

#Restriccion de Jugador 3 o Jugador 6
P.add_constraint(y[2]+y[5] <= 1)

#Restriccion de que debe estar o 2 o 3 obligatoriamente
P.add_constraint(y[1]+y[2] >= 1)

P.solve(solver= 'glpk')
print('Que jugadores van? y=\n', y)
print(P.value)