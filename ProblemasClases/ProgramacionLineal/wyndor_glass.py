# importamos las librerias a utilizar
import numpy as np 
import picos

# Inicio el problema en picos
P = picos.Problem()

# Defino las variables de decisión
x = picos.RealVariable('x', 2, lower=0)

# Defino la función objetivo
P.set_objective('max', 3000*x[0] + 5000*x[1])

# Defino las restricciones
P.add_constraint(x[0] <= 4)
P.add_constraint(2 * x[1] <= 12)
P.add_constraint(3 * x[0] + 2 * x[1] <= 18)

P.options.verbosity = 0

# Printeo el problema
print("\nResumen del problema:")
print(P)

# Resuelvo
print("\nResolviendo el problema...")
P.solve()

# Printeo las variables de decisión óptimas
print("\n\nResultados:")
print("Punto Óptimo:")
print("X1 = ", x[0])
print("X2 = ", x[1])

# Printeo el valor óptimo para la función objetivo obtenido
print("\nValor Óptimo:")
print("z* = ", P.value)