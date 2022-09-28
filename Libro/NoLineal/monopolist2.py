"""
A monopolist producing a single product has two types of customers. If q1 units are produced
for customer 1, then customer 1 is willing to pay a price of 70  4q1 dollars. If q2
units are produced for customer 2, then customer 2 is willing to pay a price of 150 
15q2 dollars. For q  0, the cost of manufacturing q units is 100  15q dollars. To maximize
profit, how much should the monopolist sell to each customer?
"""
#Problema no lineal
from scipy import optimize
import numpy as np

def f_obj(x):
    beneficio = x[0]*(70 - 4*x[0]) + x[1]*(150 - 15*x[1])
    costo = 100 + 15*x[0] + 15*x[1]

    return -(beneficio - costo)

bounds = [(0, None), (0, None)]

opt = optimize.minimize(f_obj, [1,1], bounds=bounds)

print(opt.x)

print('Beneneficio', -f_obj(opt.x))