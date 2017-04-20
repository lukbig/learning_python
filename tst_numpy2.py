import numpy as np

a1 = np.array([[2,3,4,5], [2,3,4,1]])
print('array: ' + str(a1))
print('array dimension: ' + str(a1.ndim))
print('array shape: ' + str(a1.shape))
print('array size: ' + str(a1.size))
print('array dtype: ' + str(a1.dtype))


#reshape
print('reshape first row of array: ' + str(a1[0,:].reshape(2,2)))
#[1, :] is the same as [1, ...]

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
c1 = np.arange(15)
print('c1: ' + str(c1))
b1 = c1 > 9
print('b1 = c1 > 9: ' + str(b1))
c1[b1] = 1
print('c1[b1] = 1: ' + str(c1))


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<min, max, sum>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<min, max, sum')
c2 = np.arange(25).reshape(5,5)
print('max of c2: ' + str(c2.max()))
print('min of c2: ' + str(c2.min()))
print('sum of c2: ' + str(c2.sum()))

print('cumsum of c2: ' + str(c2.cumsum()))
print('c2.max(axis=0): ' + str(c2.max(axis = 0))) # 0 for collumn, 1 for rows
print('c2.max(axis=0): ' + str(c2.max(axis = 1))) # 0 for collumn, 1 for rows


#deep copy
c3 = c2.copy()
c2[0,0] = 1
print('deep copy of c2 is c3: ' + str(c3))

#<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>hstack, vstack
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<hstack, vstack>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
v1 = np.array([2,3,4])
v2 = np.array([3,6,2])
print(np.vstack((v1, v2)))
print(np.hstack((v1, v2)))