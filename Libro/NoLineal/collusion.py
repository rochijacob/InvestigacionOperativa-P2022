"""
(Collusive Duopoly Model) There are two firms
producing widgets. It costs the first firm q1 dollars to produce
q1 widgets and the second firm 0.5q2
2 dollars to produce q2
widgets. If a total of q widgets are produced, consumers
will pay $200  q for each widget. If the two manufacturers
want to collude in an attempt to maximize the sum of their
profits, how many widgets should each company produce?
"""

#Problema no lineal

from scipy import optimize
import numpy as np

def f_obj(x):
    costo = x[0] + 0.5*x[1]**2
    q = x[0] + x[1]
    beneficio = (200- q)*x[0] + (200-q)*x[1]

    return -(beneficio - costo)

bounds = [(0, None), (0, None)]

opt = optimize.minimize(f_obj, [1,1], bounds=bounds)

print(opt.x)

print('Beneneficio', -f_obj(opt.x))