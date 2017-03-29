#defining function
def function():
	print("inside first function.")
	return "return value"

#invocation
var1 = function()
print(var1)

#multiple return values
def multival():
	return "sth", 1
print(multival())

#passing parameters
def add(a, b):
	return (a + b)

var2 = add(2,3)
print('result of addition is {0}'.format(var2))

#default values
def default_values(a, b = 2, c = 1):
	return (a + b + c)

print('default values:')
print(default_values(2))


#nested functions
def outter(a):
	def nested(b):
		# semicolon here needed, warning watch scope!
		return b * a;
	return nested(a)

print('outter: {0}'.format(outter(3)))

#function agregation
def f(a):
	def g(b):
		return a * b;
	return g
print('result of function agregation')
print(f(2)(5))

#recursive function
def factorial(n):
	if n == 1:
		return 1
	return n * factorial(n - 1)

print('factorial 5: {0}'.format(factorial(5)))

def tail_sum(n, accumulator = 0):
	if n == 0:
		return accumulator
	else:
		return tail_sum(n - 1, accumulator + n)

print('tail sum for 5: {0}'.format(tail_sum(5)))

#lambda functions - anonymous function
h = lambda x, y: x + y
print('lambda h: {0}'.format(h(2, 5)))
#nested lamba function
function1 = lambda a: lambda b: lambda c: a * b *c;
print('nested lambda function: {0}'.format(function1(5)(3)(2)))