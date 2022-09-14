import picos

P = picos.Problem()
x = picos.RealVariable('x', 9, lower = 0)
P.set_objective('max', x[0]+x[1]) #Quiero que el flujo que salga sea el maximo

flujos = [9, 7, 7, 2, 4, 6, 3, 6, 9]

for i in range(len(flujos)):
  P.add_constraint(x[i] <= flujos[i])

for j in range(2):
  P.add_constraint(x[j] == x[j + 1] + x[j + 2])

P.add_constraint(x[2]+x[4]==x[6]+x[7])
P.add_constraint(x[3]+x[5]+x[6]==x[8])

P.solve()
print('x=',x)
print(round(P.value))