""" Problema de planificación eléctrica"""

import picos


# Introduzco todas las constantes
# Demanda de cada año
demanda = picos.Constant('demanda', [80, 100, 120, 140, 160])
# Límite de producción de cada planta
x_lim = picos.Constant('x_lim', [70, 50, 60, 40])
# Costo de construcción  de cada planta
c = picos.Constant('c', [20, 16, 18, 14])
# Costo de operación anual de cada planta (una vez construída)
o = picos.Constant('o', [1.5, 0.8, 1.3, 0.6])

P = picos.Problem()

x = picos.RealVariable('x', (4,5), lower = 0)
alpha = picos.BinaryVariable('alpha', (4,5))
y = picos.BinaryVariable('y', 4)


"""
Notación:
x[i,:] refiere a tomar la fila i entera
x[:,i] refiere a tomar la columna i entera
"""

# Restricción especial: 
# Si y_i es 0 entonces la planta i no será construida y la fila x_i será toda 0
# Si y_i es 1 entonces la planta i es construída en algún momento y 
# por lo tanto la suma de la energía generada por esa planta será mayor a 0.
P.add_list_of_constraints([x[i,:].sum <= 1e4*y[i] for i in range(4)])


# Restricción especial: 
# Si alpha_ij es 0 entonces x_ij es 0.
# Si alpha_ij es 1 entonces x_ij va de 0 a lo que pueda producir esa planta
# en un año.
P.add_constraint(x <= 1e4*alpha)
P.add_list_of_constraints([x[i,:] <= x_lim[i] for i in range(4)])

# Una vez construída, la planta seguirá en operación, entonces si
# alpha_ij es 1, en consecuencia #alpha_ij+1 también es 1
P.add_list_of_constraints([alpha[:,j+1] >= alpha[:,j] for j in range(4)])

# Año a año, la suma de energía generada debe ser igual a la demanda anual.
P.add_list_of_constraints([x[:,j].sum == demanda[j] for j in range(5)])

# Función objetivo
P.set_objective('min', c.T * y + o[0] * alpha[0,:].sum + o[1] * alpha[1,:].sum + o[2] * alpha[2,:].sum + o[3] * alpha[3,:].sum)




print(P, '\n')

P.solve(solver = 'glpk')


print('Matriz de decisión X:')
print(x, '\n')
print('Matriz de decisión alpha:')
print(alpha, '\n')
print('Vector de decisión y:')
print(y, '\n')
print( 'z_opt =', P.value )