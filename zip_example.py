x = [1, 2, 3]
y = [4, 5, 6]

#zip(*iterables) Make an iterator that aggregates elements from each of the iterables.
zipped = zip(x,y)
for i in zipped:
	print(i)
'''ouput:
	(1, 4)
	(2, 5)
	(3, 6)
'''

print('list of zipped: ' + str(list(zipped)))