"""
Una compañia debe cumplir en tiempo y forma con la siguiente demanda: 30 mil unidades en el 1er trimestre, 20 mil en el 2ndo, 40mil en el 3ro. En cada trimestre puede producir hasta 27mil unidades en tiempo regular a un costo de $40 por unidad, y puede producir una cantidad ilimitada de unidades en horas extra a un \$60 costo por unidad. 

Debido a faltas de produccion el 20% de lo producido en un trimestre (ya que esta en tiempo regular o horas extra) tiene faltas de calidad y no puede ser utilizado para suplir la demanda (solo el 80% de las unidades producidas pueden ser vendidas)

Si al finalizar cada trimestre hay un excedente que se guarda por el proximo trimestre, se aplica un costo de almacenamiento de \$15 por unidad. Cual es la estrategia de produccion y almacenamiento optima para satisfacer con la demanda con minimo costo?
"""

import picos
import numpy as np

P = picos.Problem()

x_rt = picos.RealVariable('x_rt', 3, lower=0, upper=27)
x_ot = picos.RealVariable('x_ot', 3, lower=0)
x_e = picos.RealVariable('x_e', 3, lower=0) #uno menos porque no tengo cantidad almacenada incialmente

P.set_objective('min', 40*picos.sum(x_rt) + 60*picos.sum(x_ot) + 15*picos.sum(x_e))



P.add_constraint((x_rt[0] + x_ot[0])*0.8 + 0 - x_e[0] == 30)
P.add_constraint((x_rt[1] + x_ot[1])*0.8 + x_e[0] - x_e[1] == 20)
P.add_constraint((x_rt[2] + x_ot[2])*0.8 + x_e[1] - x_e[2] == 40)


P.solve(solver='glpk')

print('Regular time: \n', x_rt)
print('Over time: \n', x_ot)
print('Almacenaje: \n', x_e)
print(P.value)
