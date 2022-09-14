import picos

P = picos.Problem()
X = picos.RealVariable('X', (4,5), lower = 0)

# Matriz de costo
C = picos.Constant('C', [[8,13,25,28,0], [15,12,26,25,0], [0,6,16,17,0], [6, 0, 14, 16,0]])

# Funcion objetivo a minimizar
# Producto interno: multiplica elemento a elemento y suma todo
P.set_objective('min', C|X)

# Oferta total
S = 350

# Demanda total
D = 260

# Condiciones de oferta
P.add_constraint(picos.sum(X[0,:]) <= 150)  # s_1
P.add_constraint(picos.sum(X[1,:]) <= 200)  # s_2
P.add_constraint(picos.sum(X[2,:]) <= 0 + S)  # s_3
P.add_constraint(picos.sum(X[3,:]) <= 0 + S)  # s_4

# Condiciones de demanda
P.add_constraint(picos.sum(X[:,0]) == 0 + S)  # d_1 
P.add_constraint(picos.sum(X[:,1]) == 0 + S)  # d_2
P.add_constraint(picos.sum(X[:,2]) == 130)    # d_3
P.add_constraint(picos.sum(X[:,3]) == 130)    # d_4
P.add_constraint(picos.sum(X[:,4]) == S-D)    # d_5 (punto de demanda ficticio)

P.solve()

print(X)
print(P.value)