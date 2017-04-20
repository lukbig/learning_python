#numpy - multi dimensional arrays and matrixes
import numpy as np

a1 = np.array([2,1,3,4])
a2 = np.array([[1,2,1],[2,1,2], [1,2,3]])
print(a1)
print('a2: ' + str(a2))


# jak w matlabie a4 = [10 : 10 : 50] tylko tutaj jest bez 50
# output w matlabie: [10, 20, 30, 40, 50]
# ouput w pythonie: [10, 20, 30, 40]
a4 = np.arange(10, 50, 10)
print('a4 created with arange: ' + str(a4))

a5 = np.arange(5)
print('a5 arange(5): ' + str(a5))

a6 = np.arange(5, 8)
print('a6 arange(5,8): ' + str(a6))

#floats:
a7 = np.arange(0.3, 2, 0.2)
print('floats: ' + str(a7))

#linspace
# 9 steps from 3 to 8
a8 = np.linspace(3, 8, 9)
print('linspace(3,8,9)  9 steps: ' + str(a8))

o1 = np.ones((2,2))
print('ones((2,2)) - 2x2 matrix: ' + str(o1))

z1 = np.zeros((2,2))
print('zeros: ' + str(z1))

e1 = np.eye(2)
print('eye(2): ' + str(e1))

#random
print('<<<<<<<<<<<<<<<<<<<<<random>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
r1 = np.random.random((2,3))
print('r1: ' + str(r1))