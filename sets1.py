set1 = set([1, 5, 'a', 'a'])
print('set1 with duplicated a: '  + str(set1))
set2 = set(['a', 'b', 'c'])
#union of set1 and set2
set3 = set1 | set2
print('set3 - union of set1 and set2: ' + str(set3))
#bez czesci wspolnej - set without common part of the collection
set4 = set1 ^ set2
print('set4 - unique elements of set1 and set2: ' + str(set4))

#checking if set1 is a subset of set2
print('is set1 a subset of set2? ' + str(set1 <= set2))

print('<<<<<<<<<<<<<<<<<<<,,addding element to the set>>>>>>>>>>>>>>>>>>>>')
set1.add('five')
print('set1 after five addition: ' + str(set1))

print('<<<<<<<<<<<<<<<<<<set functions>>>>>>>>>>>>>>>>>>>>>>>')
print('union of set1 and set2:' + str(set.union(set1, set2)))
print('intersection of set1 and set2:' + str(set.intersection(set1, set2)))
print('difference of set1 and set2:' + str(set.difference(set1, set2)))