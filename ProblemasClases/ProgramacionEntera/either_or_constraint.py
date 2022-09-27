# Dorian Auto is considering manufacturing three types of autos: compact, midsize, and
# large. The resources required for, and the profits yielded by, each type of car are shown
# in Table 8. Currently, 6,000 tons of steel and 60,000 hours of labor are available. For production
# of a type of car to be economically feasible, at least 1,000 cars of that type must
# be produced. Formulate an IP to maximize Dorian’s profit.

#Variables de descicion
import picos

P = picos.Problem()

x = picos.RealVariable('x', 3, lower=0)
y = picos.BinaryVariable('y', 3) #si produzo o no produzco

P.set_objective('max', 2*x[0] + 3*x[1] + 4*x[2])

#Los autos pueden usar como mucho 6000 toneladas de acero y 60000 horas de trabajo

P.add_constraint(1.5*x[0] + 3*x[1] + 5*x[2] <= 6000)
P.add_constraint(30*x[0] + 25*x[1] + 40*x[2] <= 60000)

#Para que sea economicamente viable producir al menos 1000 autos de cada tipo 
#EITHER OR CONSTRAINT
M = 2000

P.add_list_of_constraints(x[i] <= M*y[i] for i in range(3))
P.add_list_of_constraints((1000 - x[i]) <= M*(1-y[i]) for i in range(3))

P.solve()

print('Fabricacion')
print(x)
print('Produccion o no produccion')
print(y)
print('Valor de la funcion objetivo', P.value)