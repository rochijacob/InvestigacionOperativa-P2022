import picos
import numpy as np
#Problema de transhipment
P = picos.Problem()

#Voy a tener un solo vector con todas mis variables, tengo nodos que envian, almacenan y reciben, y esto lo voy a expresar mediante mis restricciones
x = picos.RealVariable('x', 14, lower=0)
c = np.array([10, 12, 15, 20, 15, 10, 12, 12, 10, 15, 14, 25, 30, 5])
c = picos.Constant('c', c, (1, 14)) #Le defino la direccion para poder multiplicarlo

P.set_objective('min', c*x) #Quiero minimizar mi costo de transporte: lo que paso de nodo a nodo

#Array de lo que puede transportar cada nodo en ORDEN

t = [50, 100, 100, 200, 200, 200, 200, 100, 100, 100, 100, 25, 150, 50]

P.add_list_of_constraints(x[i] <= t[i] for i in range(len(t))) #Restriccion de que no puede transportar mas de lo que puede

#Restriccion de Oferta (<=)

P.add_constraint(x[0] + x[1] + x[2] <= 100)
P.add_constraint(x[3] + x[4] <= 175)
P.add_constraint(x[5] + x[6] <= 200)

#Restriccion de Demanda (==)

P.add_constraint(x[0] + x[9] + x[11] + x[13] == 200)
P.add_constraint(x[10] + x[12] == 100)

#Restriccion de Almacenes (transhipment)

P.add_constraint(x[1] + x[3] + x[5] + x[7] == x[8] + x[9] + x[10])
P.add_constraint(x[2] + x[4] + x[6] + x[8] == x[7] + x[11] + x[12])

P.solve()

print('Cantidad a transportar por mes:')
print(x)
print('Costo minimo', P.value)

