"""
It costs a monopolist $5/unit to produce a product. If he produces x units of the product,
then each can be sold for 10  x dollars (0  x  10). To maximize profit, how much
should the monopolist produce?
"""
#Problema No Lineal
from scipy import optimize
import numpy as np

def f_obj(x):
    return -(5*x - x**2)

bounds = [(0, 10)]

opt = optimize.minimize(f_obj, 1, bounds=bounds)

print(opt.x)