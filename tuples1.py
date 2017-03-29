#tuple - krotka, para uporzadkowana
#sequence of immutable objects, objects cannot be changed

tup = (1, 'abc', 2, 'cde')
tup1 = 3, 'efg', True
tup2 = 'A',	#defining single element tuple

#printing all memembers of tuples
print('tuple 0: {0}'.format(tup))
print('tuple 1: {0}'.format(tup1))
print('tuple 2: {0}'.format(tup2))

#printing element of tuple
print("element 0 of tuple 0 is <<<<<<< {0} >>>>>>>>>>".format(tup[0]))
print("elements 0 and 1 of tuple1 are <<<<<<<<<< {0} >>>>>>>>".format(tup1[0:2]))

# try assign value to tuple
try:
	tup[3] = 5
except Exception as e:
	print(e)

#addition
tup = tup[0:3] + (5,)
print('tuple after addition: ' + str(tup))
#multiplication
print('tuple after multiplication: ' + str(tup2 * 4))
#in
print('abc in the tuple?: ' + str('abc' in tup))

print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<LOOPS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#loops
print('iterating in a tuple:')
for x in tup:
	print(str(x) + ' ', end = "")
print()
