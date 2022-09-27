import picos

P = picos.Problem()

y = picos.BinaryVariable('y', 5)

#Valor del contrato - lo que le cuesta  a la empresa
P.set_objective('max', (80000 - 1500*40)*y[0] + (20000 - 1250*40)*y[1] + (60000 - 1000*40)*y[2] + (40000 - 750*40)*y[3] + (100000 - 1750*40)*y[4])

#No puede superar los 150000 la inversion
P.add_constraint((1500*40)*y[0] + (1250*40)*y[1] + (1000*40)*y[2] + (750*40)*y[3] + (1750*40)*y[4] <= 150000)

P.solve(solver='glpk')

print('La empresa debe tomar los contratos: ')
print(y)
print(f'En total gana {P.value} con los contratos')