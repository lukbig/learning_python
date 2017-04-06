list1 = [1, 'abc', (2,3)]
print('printing list: ' + str(list1))
print('2 copies of entire list: ' + str(list1 * 2))
print('is 1 in a list1: ' + str(1 in list1))

#appending list
list1.append('sth')
print('appened list with sth: ' + str(list1))

list1[len(list1):] = ['new sth']
print('appened list with new sth: ' + str(list1))

#functions on list
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,,,functions on list>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#syntax for map: map(function, list)
list2 = list(map(lambda x: x**2 + 3*x + 1, [1, 2, 3, 4]))
print('map on list [1, 2, 3, 4] with function x^2 + 3x + 1: ' + str(list2))

#syntax for filter: filter(function, list)
list3 = list( filter (lambda x: x < 4, [1, 2, 3, 4, 5, 6, 7, 7]) )
print('filter on list [1, 2, 3, 4, ...] with condition x < 4: ' + str(list3))

#syntax for reduce: functools.reduce(function, list), packet functools need to be imported
import functools
list4 = functools.reduce( lambda x, y: x * y, [1, 2, 3, 4] )
print('reduce on list [1,2,3,4]: ' + str(list4))