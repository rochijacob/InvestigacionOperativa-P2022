import matplotlib.pyplot as plt
import numpy as np
import picos

# 100 linearly spaced numbers
x = np.linspace(-5,5,100)
y = x**2

w = []

r = -5
while r < 95:
  r = r +1
  w.append(2)

w = np.array(w)

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'r')
plt.plot(x, w, 'b')

# show the plot
plt.show()

P = picos.Problem()
x = picos.RealVariable('x',1)
P.set_objective('min', x[0]**2)
P.add_constraint(x[0]>=2)
P.options.verbosity = 1
print(P)
P.solve()
print('punto optimo', round(x))
print('valor optimo', round(P.value))