def function(x, y):
  #Condiciones
  one = (2*x + 3*y <= 24)
  two = (x > 0)
  three = (y > 0)
  if(one and two and three):
    print('true')
    return True
  else:
    print('false')
    return False

x = int(input('Ingresa un numero:' ))
y = int(input('Ingresa otro numero:' ))

function(x, y)

