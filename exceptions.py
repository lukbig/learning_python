#exception handling

try:
	a = 5/0
except Exception as e:
	print('exception: {0}'.format(e))
finally:
	print('testing try')

try:
	#trying to do parseInt
	n = int('a')
except ValueError:
	print("that is not an integer.")
''' here can be another exception for example:
except ZeroDivisionError:
	pitu pitu
except IOError:
	another pitu pitu
'''

#throwing exception - raise exception
print('<<<<<<<<<<<<<<<<<<<<<<<<<Throwing exception>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

a = 1

def RaiseException(a):
	if type(a) != type('a'):
		raise ValueError("This is not a string")

try:
	RaiseException(a)
except Exception as e:
	print(e)

#test case
print('<<<<<<<<<assertions>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
def TestCase(a, b):
	assert a < b, "a is greater than b"

try:
	TestCase(2, 1)
except AssertionError as e:
	print(e)