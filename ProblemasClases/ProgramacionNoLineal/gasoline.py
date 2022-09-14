from scipy import optimize
import numpy as np


# Parametros - Gasolina
price_gasoline = [0.86, 0.93, 1.06]
demand = [5000, 5000, 5000]
sulphur_gasoline = [3., 3., 2.8]
octane_gasoline = [90, 88, 94]
# Parameteros - Recursos
cost_input = [0.78, 0.88, 0.75, 1.3]
sulphur_input = [4., 1., 2., 0]
octane_input = [91, 97, 83, 800]


# Funcion objetivo
def target_function(x):
    # len(x) = 12
    x = np.array(x)
    # Cambiamos el formato de las variables de decision.
    x = x.reshape((4, 3))
    z = 0
    for alpha in range(3):
        z += x[:, alpha].sum() * price_gasoline[alpha]
    for i in range(4):
        z -= x[i, :].sum() * cost_input[i]
    return -z 


# Restricciones 
def sulphur_octave_constraint(x):
    # len(x) = 12
    x = np.array(x)
    # Cambiamos el formato de las variables de decision.
    x = x.reshape((4, 3))
    output = []
    # Restriccion de azufre
    for alpha in range(3):
        output.append(x[:, alpha].dot(sulphur_input)/x[:, alpha].sum())
    # Restriccion de octano
    for alpha in range(3):
        output.append(x[:, alpha].dot(octane_input)/x[:, alpha].sum())
    return output


def supply_demand_constraint(x):
    x = np.array(x)
    # Cambiamos el formato de las variables de decision.
    x = x.reshape((4, 3))
    output = []
    # Restricciones de Demanda
    for alpha in range(3):
        output.append(x[:, alpha].sum())
    # Restricciones de oferta
    output.append(x[0, :].sum() + x[1, :].sum())
    output.append(x[2, :].sum())
    output.append(x[3, :].sum())
    return output

def unleaded_gas_constraint(x):
    x = np.array(x)
    # Cambiamos el formato de las variables de decision.
    x = x.reshape((4, 3))
    # Restriccion de Gasolina sin plomo
    return x[3, 1]

constraint1 = optimize.NonlinearConstraint(sulphur_octave_constraint, lb=[0, 0, 0, octane_gasoline[0], octane_gasoline[1], octane_gasoline[2]], ub=[sulphur_gasoline[0], sulphur_gasoline[1], sulphur_gasoline[2], np.inf, np.inf, np.inf])
constraint2 = optimize.NonlinearConstraint(supply_demand_constraint, lb = [demand[0], demand[1], demand[2], 0, 0, 0], ub=[np.inf, np.inf, np.inf, 10000, 11000, 6000])
constraint3 = optimize.NonlinearConstraint(unleaded_gas_constraint, lb = [0], ub=[0])

constraints = [constraint1, constraint2, constraint3]

bounds = [(0, np.inf) for _ in range(12)]
x0 = 12*[1]
opt = optimize.minimize(fun=target_function, x0=x0, bounds=bounds, constraints=constraints)

print('Valor óptimo: ' , opt.fun)
print('Punto óptimo: ')
print(np.array(opt.x).reshape((4, 3)).round(3))


