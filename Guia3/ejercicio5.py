import picos
import numpy as np
#Ejercicio 5
#Sunny Skies unlimited planeacion estrategica


P = picos.Problem()

x= picos.BinaryVariable('x',(5,5))
y = picos.BinaryVariable('y', 5)

c=np.array([[10,12,90,20,45],
            [40,4,45,10,75],
            [30,20,18,15,36],
            [50,15,75,4,30,],
            [20,25,45,12,15],])

#La frecuencia suma 10
#P.set_objective('min',c|x)
P.set_objective('min', 1/10*( 2*picos.sum(c[:,0]^x[:,0]) + 1*picos.sum(c[:,1]^x[:,1]) + 3*picos.sum(c[:,2]^x[:,2]) + 1*picos.sum(c[:,3]^x[:,3]) + 3*picos.sum(c[:,4]^x[:,4]) ))


##una sola estacion por sector
P.add_list_of_constraints(sum(x[:, i]) == 1 for i in range(5))

#la respuesta no puede venir de una estacion q no se construye
P.add_constraint(x[0,:]<=y[0]*5)
P.add_constraint(x[1,:]<=y[1]*5)
P.add_constraint(x[2,:]<=y[2]*5)
P.add_constraint(x[3,:]<=y[3]*5)
P.add_constraint(x[4,:]<=y[4]*5)



P.add_constraint(sum(y)==2)

P.solve(solver= 'glpk')
print('x=', x)
print('y=', y)
print(P.value)