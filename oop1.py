#defining class

class Complex:
	'doc string, this class simulates complex numbers'
	# self must be placed first
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag

c = Complex(1, 1)
print(c.real, c.imag)

try:
	c1 = Complex(2)
except Exception as e:
	print(e)

# class with default values
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<class with default values>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
class Complex1:
	def __init__(self, real = 0, imag = 0):
		self.real = real
		self.imag = imag

c2 = Complex1()
print(c2.real, c2.imag)

# checking arguments
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<checking arguments>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
class Complex2:
	def __init__(self, r, i):
		if ((type(r) not in (int, float)) or (type(i) not in (int, float))):
			raise Exception('arguments are not number!')
		self.r = r
		self.i = i

try:
	c3 = Complex2('a', 2)
except Exception as e:
	print(e)

# methods
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<methods>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
class Complex3:
	def __init__(self, r, i):
		if ((type(r) not in (int, float)) or (type(i) not in (int, float))):
			raise Exception('arguments are not number!')
		self.r = r
		self.i = i

	def getReal(self):
		return self.r
	def getImag(self):
		return self.i
	def setReal(self, r):
		self.r = r
	def setImag(self, imag):
		self.i = imag

c4 = Complex3(1.0, 3.5)
print('getting parameters with methods')
print(c4.getReal(), c4.getImag())

print('set new values to parameters')
c4.setReal(5.3)
c4.setImag(6.2)
print(c4.getReal(), c4.getImag())
print('accessing not private value (c4.r): ' + str(c4.r))

# defining parameters as private <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class Complex4:
	def __init__(self, r = 0, i = 0):
		if ((type(r) not in (int, float)) or (type(i) not in (int, float))):
			raise Exception('arguments are not number!')
		self.__r = r
		self.__i = i

	def getReal(self):
		return self.__r
	def getImag(self):
		return self.__i
	def setReal(self, r):
		if type(r) not in (int, float):
			raise Exception('r is not number!')
		self.r = __r
	def setImag(self, imag):
		if type(imag) not in (int, float):
			raise Exception('imag is not number!')
		self.__i = imag

	#toString() overloading
	def __str__(self):
		return str(self.getReal()) + ' + j' + str(self.getImag())
	# add overloading
	def __add__(self, other):
		return Complex4(self.getReal() + other.getReal(), self.getImag()  + other.getImag())
	#multiplication
	def __mul__(self, other):
		if type(other) in (int, float):
			return Complex4(self.getReal() * other, self.getImag() * other)
		else:
			return Complex4(self.getReal() * other.getReal() - self.getImag() * other.getImag(), self.getImag() * other.getImag() + self.getReal() * other.getReal())
	#division
	def __truediv__(self, other):
		if type(other) in (int, float):
			return Complex4(self.getReal() / float(other), self.getImag() / float(other))
		else:
			a, b, c, d = self.getReal(), self.getImag(), other.getReal(), other.getImag()
			nominator = c * c + d * d
			return Complex4((a * c + b * d) / nominator, (b * c - a * d) / nominator)

c5 = Complex4()
try:
	c5.setReal((1,2,3))
except Exception as e:
	print(e)

#testing operator overloading
print('print c5 to str: ' + str(c5))
# adding with + operator, with method overloaded
print('c5 + new complex(1,4): ' + str(c5 + Complex4(1, 4)))

# operator overloading
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<operator overloading>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
a = Complex4(2.2, 5.1)
b = Complex4(-3, 7)
print("addition: " + str(a + b))
print("multiplication: " + str(a * b))
print("division: " + str(a / b))