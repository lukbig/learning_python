#deep cop
import copy

my_dictionary = {'key1': 1, 'key2': 2}
my_dictionary1 = copy.deepcopy(my_dictionary)
my_dictionary['key2'] = 'abc'
print('after deep copy and change key2, my_dictionary: ' + str(my_dictionary))
print('after deep copy and change key2, my_dictionary1: ' + str(my_dictionary1))

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<MATH MODULE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<MATH MODULE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
import math as m
print('exponent of 2: ' + str(m.exp(2)))
print('cos of pi: ' + str(m.cos(m.pi)))
print('ceiling of 2.14: ' + str(m.ceil(2.14)))

import cmath as cm
print('show function of cmath: ' + str(dir(cm)))
print('sqrt of 2: ' + str(cm.sqrt(2)))

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<random module>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<random module>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
import random as rand
print('random.sample of [1,2,3,4,5]: ' + str(rand.sample([1, 2, 3, 4, 5], 3)))
print('random <0,1>: ' + str(rand.random()))
print('random int from interval: ' + str(rand.randint(5,100)))

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<SYS MODULE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<SYS MODULE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
import sys
print('recursion limit: ' + str(sys.getrecursionlimit()))
print('version of python: ' + str(sys.version))