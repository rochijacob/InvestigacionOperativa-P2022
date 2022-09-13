import picos

P = picos.Problem()
x = picos.RealVariable('x',1)
P.set_objective('max', x[0])
P.add_constraint(x[0]>=0)
P.add_constraint(x[0]<=10)
P.options.verbosity = 1
#print(P)
P.solve()
print('Optimal Point', x)
print('Optimal Value:', P.value)