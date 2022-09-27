"""
Un banco quiere determinar en que invertir \$500000 este año. Puede distribuir la inversion de este dinero en cuatro cosas: bonos, prestamos hipotecarios, prestamos vehiculares (prestamos para comprar un automovil) o prestamos personales. El retorno anual de cada una de estas inversiones es: 10%, 16%, 13% y 20% respectivamente (es decir si invierto \$1 a fin deaño recibo $1.1). Para asegurar que el portfolio de inversiones no sea riesgoso, el banco requiere que se cumplan las siguientes condiciones:
1. La cantidad de dinero invertida en creditos personales no puede exceder lo invertido en bonos
2. La cantidad de dinero invertida en creditos hipotecarios no puede exceder lo invertido en prestamos vehiculares
3. La cantidad invertida en prestamos personales no puede ser mas que el 25% invertido. 

Si el banco quiere maximizar el retorno anual de la inversion ¿Cual es la estrategia de inversion optima y cual es el retorno maximo?
"""

import picos

P = picos.Problem()

x = picos.RealVariable('x', 4, lower=0)

P.set_objective('max', 1.1*x[0] + 1.16*x[1] + 1.13*x[2] + 1.2*x[3])

# La cantidad de dinero que se puede invertir

P.add_constraint(x[0] + x[1] + x[2] + x[3] <= 500000)

# Dinero en creditos personales no puede exceder al bono

P.add_constraint(x[3] <= x[0])
P.add_constraint(x[1] <= x[2])
P.add_constraint(x[3] <= 0.25*(x[0] + x[1] + x[2] + x[3]))

P.solve(solver='glpk')

print(x)
print(P.value)