"""
It costs a company $6/unit to produce a product. If it
charges a price p and spends a dollars on advertising, it can
sell 10,000p^-2(a)^1/6 units of the product. Find the price and
advertising level that will maximize the company’s profits.
"""
 
from scipy import optimize
import numpy as np

def f_obj(x):
    beneficio = (10000*x[0]**-2)*x[1]**(1/6)
    costo = 6*x[0] + x[1]
    return -(6*x[0])