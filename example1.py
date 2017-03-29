print("welcome")
print("working with comments")
# single line comment
#single line comment

''' multi line comments
	next line
	next line
	next line
'''

#arithmetic
print(2.0 + 5)
print(2 + 5)
var1 = 30 * 50
print(var1)
print(2**5)

#division with floor value
print(23//5)

#priorities
# (), **, *, /, %, +, -
print(25*10 + 33/2.0)

# shift
print(1 << 3) # its 8,  2_0, 2_1, 2_2, 2_3
print(32 >> 3)
#binary operators
print('binary operators')
print(254 & 253)
print(256 | 255)
# 00111100
# 00001101
print(60 ^ 13)
# 00110001 - 49

# String
str1 = 'str1'
str2 = "str2"

print(str1[0])

print(str2[len(str2) - 1])
print(str2[-1])

print(str1[1:3])
print(str2[2:])

str3 = 'Concate' + 'nation'
print(str3)
str4 = 2 * ('ab' 'cd')
print(str4)
str5 = 'con'
str6 = 'catenate'
print(str5 + str6)

# formatting
print("Today I had {0} cups of {1}".format(3, "coffee"))
print("prices: ({x}, {y}, {z})".format(x = 2.0, y = 1.5, z = 5))
print('The {vehice} had {0} crashes in {1} months'.format(5, 6, vehice = 'car'))
# left & right aligment
print('{:<20}'.format("text"))
print('{:>20}'.format("text"))
# binary, hex, octal
print('binary 21: {:b}'.format(21))
print('hexa 21: {:x}'.format(21))
print('octal 21: {:o}'.format(21))

# backslash etc
print("lalal\"dfafd")
print(r'c:\number\nan')
print("""\
	Hello:
		ballalal
		fdaf
		""")

# conditional operators
######################################################################################
a = True
b = False
print('not a:')
print(not a)
print('a and b:')
print(a and b)
print('a or b')
print(a or b)

# if statements
result1 = True
result2 = True

if result1 and result2:
	print("hello, I am inside if")
elif result1:
	print('sth')
else:
	print('whatever')

'''
if condition1:
	do sth
elif condition2:
	do sth
else:
	do sth
	'''
#ternary operator
me = 'hi' if result1 == False else 'Hey'
print("me:")
print(me)

#loops
for i in range(1,3):
	print(i)
''' in other programming language, python for loop is
equivalent to
for (int i = 1; i < 3; i++)
'''
str7 = 'String traversal'
for i in range(len(str7)):
	if (str7[i] == 'i'):
		print('letter: \'i\' captured at index {0}'.format(i))

for char in str7:
	if (char == 'i'):
		print('found i')

# multiplication table
for i in range(1,11):
	#,end="" means print in one line
	print('{:<3}|'.format(i), end = "")

	for j in range(1,11):
		print('{:>4}'.format(i * j), end = "")

	if i == 1:
		print('\n{:#^44}'.format(""), end = "")

	# new line
	print("")

#####################################################################
# while loop
condition3 = True
while condition3:
	print('inside while', end = "\t")
	print("xD")
	condition3 = False