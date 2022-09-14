# Maximum Flow Example

# Import libraries
import numpy as np
import picos

# Create Picos problem
p = picos.Problem()

# Variables
x = picos.RealVariable('x', 6, lower = 0, upper = [2, 3, 4, 3, 1, 2])

# Constraints
p.add_constraint(x[0] == x[2] + x[3])
p.add_constraint(x[3] + x[1] == x[5])
p.add_constraint(x[2] == x[4])

# Objective function
p.set_objective('max', x[0] + x[1])

# Print problem summary
print(p)

# Solve 
p.solve(solver = 'glpk')

# Print solution
for i in range(len(x)):
    print('x'+str(i+1)+'* =', round(x[i],2) )

print( 'z* =', round(p.value) )