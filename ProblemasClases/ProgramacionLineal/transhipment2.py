# Transshipment Example

# Import libraries
import numpy as np
import picos

# Define model parameters
a1 = np.array([[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]])

a2 = np.array([[ 1, 0, 0, 0, 1, 0, 0, 0,-1,-1,-1, 0, 0, 0],
                [ 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0,-1,-1, 0],
                [ 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0,-1],
                [ 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1,-1]])


c = np.array([10, 12, 45, 28, 5, 12, 26, 25, 6, 16, 17, 14, 16, 15])

b1 = np.array([150, 200])

b2 = np.array([0, 0, 140, 160])

# Create Picos problem
p = picos.Problem()

# Variables
x = picos.RealVariable('x', 14, lower = 0)

# Constraints
c = picos.Constant('c', c, (1,14))
a1 = picos.Constant('a1', a1)
a2 = picos.Constant('a2', a2)
b1 = picos.Constant('b1', b1, (2,1))
b2 = picos.Constant('b2', b2, (4,1))
p.add_constraint(a1*x <= b1)
p.add_constraint(a2*x == b2)

# Objective function
p.set_objective('min', c*x)

# Print problem summary
print(p)

# Solve 
p.solve(solver = 'glpk')

# Print solution
for i in range(len(x)):
    print('x'+str(i+1)+'* =', round(x[i],2) )

print( 'z* =', round(p.value) )