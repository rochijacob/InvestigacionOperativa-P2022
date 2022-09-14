import picos

P = picos.Problem()
x = picos.RealVariable('x', 2, lower=[0,0])

#Funcion Objetivo

P.set_objective('max', 180*x[0] + 90*x[1])

#Restricciones

P.add_constraint(6*x[0]+8*x[1] <= 48)
P.add_constraint(x[1] == 4)
P.add_constraint(x[0] <= 6)

#Resolucion de la optimizacion

P.solve(solver='glpk')

#Solucion

print(f'Deben fabricar {round(x[0])} marcos de madera')
print(f'Deben fabricar {round(x[1])} marcos de aluminio')

print('La ganancia maxima es de', P.value)