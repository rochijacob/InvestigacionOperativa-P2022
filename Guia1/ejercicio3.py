import numpy as np

my_list = [1,32,53,14,55,36,27]

#Forma 1 - For Loop


total = 1 + 32 + 53 + 14 + 55 + 36 + 27

print('Lo que me deberia dar: ', total/len(my_list))

def mean(x):
  mean = 0
  for i in my_list:
    mean = mean + i
    trueMean = mean/len(x)

  return trueMean

print('La media con el for loop: ', mean(my_list))

#Forma 2 - Con numpy

print('La media con numpy: ', np.array(my_list).mean())