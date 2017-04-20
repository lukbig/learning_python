import numpy as np

x = np.linspace(0, 6.28, 20)
print('sin of linspace like in matlab: ')
print(np.sin(x))

x1 = np.arange(9).reshape(3,3)
print(x1 > 4)

x2 = np.arange(10, 19).reshape(3,3)
#matlab multiply with dot *.
x3 = x1 * x2
print('x3 = x1 * x2: ' + str(x3)) 

#array multiplication x1.dot(x2) is the same as np.dot(x1, x2)
x4 = x1.dot(x2)
print('x4 = x1.dot(x2): ' + str(x4))