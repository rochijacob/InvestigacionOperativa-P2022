import picos

P = picos.Problem()
x = picos.IntegerVariable('x', 3, lower=0)
y = picos.BinaryVariable('y', 3) #variables que uso como switches
c = picos.Constant('c', [1, 1, 1])
M = 1000000

#Funcion Objetivo

P.set_objective('max', 2000*x[0] + 3000*x[1] + 4000*x[2])

#Restricciones

P.add_constraint(1.5*x[0] + 3*x[1] + 5*x[2] <= 6000)
P.add_constraint(30*x[0] + 25*x[1] + 40
*x[2] <= 60000)

#Construyo o no

P.add_constraint(x <= 1000*y)
P.add_constraint(x >= 1000*c - 1000*( c-y))

P.solve()

print(P.value)