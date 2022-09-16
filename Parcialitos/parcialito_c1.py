#Instalo picos: pip install picos
#Instalo swiglpk: pip install swiglpk

import picos
import numpy as np

#Arranco con PICOS
P = picos.Problem()

#Es un problema con una variable interger y otra binaria

x = picos.IntegerVariable('x', 15, lower=0) #Variable interger no olvidar el lower
y = picos.BinaryVariable('y', 5) #Variable binaria

#El problema plantea maximizar la ganancias dada la inversion

#ganancia
g = np.array([[5, 6, 0.5, 5, 4, 4.5, 5.4, 0.5, 4.5, 3.6, 4, 4.8, 0.1, 4, 3.2]])
#capital requerido
c = np.array([[7, 9, 8, 1, 6]])

P.set_objective('max', g*x - c*y)

# Restriccion de presupuesto

P.add_constraint(5*x[0]+6*x[1]+0.5*x[2]+5*x[3]+4*x[4] <= 7)
P.add_constraint(4.5*x[5]+5.4*x[6]+0.5*x[7]+4.5*x[8]+3.6*x[9] <= 8)
P.add_constraint(4*x[10]+4.8*x[11]+ 0.1*x[12]+4*x[13]+3.2*x[14] <= 10)

# Restriccion de capital

P.add_constraint(5*x[0] + 4.5*x[5] + 4*x[10] <= 7)
P.add_constraint(6*x[1] + 5.4*x[6] + 4.8*x[11] <= 9)
P.add_constraint(0.5*x[2] + 0.5*x[7] + 0.1*x[12] <= 8)
P.add_constraint(5*x[3] + 4.5*x[8] + 4*x[13] <= 1)
P.add_constraint(4*x[4] + 3.6*x[9] + 3.2*x[14] <= 6)

# Inversion 1 y 2 excluyentes

P.add_constraint(y[0] + y[1] <= 1)

#Solo realizo la 3 si se realiza la 4

P.add_constraint(y[2] + y[3] == 1*y[3])

#cada inversion se realiza una vez
P.add_constraint(x[0] + x[5] + x[10] <= 1)
P.add_constraint(x[1] + x[6] + x[11] <= 1)
P.add_constraint(x[2] + x[7] + x[12] <= 1)
P.add_constraint(x[3] + x[8] + x[13] <= 1)
P.add_constraint(x[4] + x[9] + x[14] <= 1)


P.solve(solver='glpk') #Con solver glpk

print('\n Valor Optimo de X', x)
print('\n Valor Optimo de Y', y)
print('\n Valor Optimo', P.value)

