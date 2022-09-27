import picos
import numpy as np
#Problema Regular Over Time

P = picos.Problem()

#Tengo un problema que tiene produccion en regular time y en overtime, y ademas tengo almacenaje

#Defino mis variables. Tengo 6 de produccion y 5 de almacenaje
x_rt = picos.RealVariable('x_rt', 6,  0, 200) #Produccion en regular time
x_ot = picos.RealVariable('x_ot', 6,  0, 100) #Produccion en overtime
x_a = picos.RealVariable('x_a', 5, 0)

#Defino mi funcion objetivo

#picos.sum() va a sumar todas mis variables

P.set_objective('min', 7*picos.sum(x_rt) + 11*picos.sum(x_ot) + 1*picos.sum(x_a))

#Defino mis restricciones

#Restriccion 1: Produccion en regular time + overtime + (EI almacen - EF almacen) == 200
P.add_constraint(x_rt[0] + x_ot[0] + (0 - x_a[0]) == 200)
P.add_constraint(x_rt[1] + x_ot[1] + (x_a[0] - x_a[1]) == 260)
P.add_constraint(x_rt[2] + x_ot[2] + (x_a[1] - x_a[2]) == 240)
P.add_constraint(x_rt[3] + x_ot[3] + (x_a[2] - x_a[3]) == 340)
P.add_constraint(x_rt[4] + x_ot[4] + (x_a[3] - x_a[4]) == 190)
P.add_constraint(x_rt[5] + x_ot[5] + x_a[4] - 0 == 150)

P.solve(solver='glpk')

print('Cantidad a producir en horas regulares por mes:')
print(x_rt)
print('Cantidad a producir en horas extra por mes:')
print(x_ot)
print('Cantidad a almacenar por mes:')
print(x_a)
print(P.value)
