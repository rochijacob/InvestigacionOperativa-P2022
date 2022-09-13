import picos

P = picos.Problem()
X = picos.RealVariable('X', (4,4), lower = 0)

# Matriz de costo
C = picos.Constant('C', [[8,6,10,9], [9,12,13,7], [14,9,16,5], [70, 60, 50, 40]])

# Funcion objetivo a minimizar
# Producto interno: multiplica elemento a elemento y suma todo
P.set_objective('min', C|X)

# Condiciones de oferta
P.add_constraint(picos.sum(X[0,:]) <= 35)  # s_1
P.add_constraint(picos.sum(X[1,:]) <= 50)  # s_2
P.add_constraint(picos.sum(X[2,:]) <= 40)  # s_3
P.add_constraint(picos.sum(X[3,:]) <= 15)  # s_4 (la ficticia)

# Condiciones de demanda
# Como el problema esta (nuevamente) balanceado puedo poner igualdades
P.add_constraint(picos.sum(X[:,0]) == 60)  # d_1
P.add_constraint(picos.sum(X[:,1]) == 20)  # d_2
P.add_constraint(picos.sum(X[:,2]) == 30)  # d_3
P.add_constraint(picos.sum(X[:,3]) == 30)  # d_4

P.solve()
print(X)
print(P.value)
print(C|X)