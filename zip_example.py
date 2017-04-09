x = [1, 2, 3]
y = [4, 5, 6]

#zip(*iterables) Make an iterator that aggregates elements from each of the iterables.
zipped = zip(x,y)
for i in zipped:
	print(i)

print('list of zipped: ' + str(list(zipped)))