#2 ways of declaring dictionaries:
my_dictionary = {'key1' : 'value1', 'key2' : 2, "key3" : (1, 2, 3)}
my_dictionary1 = {x : x + 1 for x in range(5)}

#printing dictionaries
print('printing dictionaries')
print('my_dictionary: ' + str(my_dictionary))
print('my_dictionary1: ' + str(my_dictionary1))

#accessing elements of dictionaries
print('<<<<<<<<<<<<<<<<<<<<<<access elements>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('getting key1 of my_dictionary: ' + str(my_dictionary['key1']))

#adding and deleting elements to/in dictionary
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#adding and deleting elements to/in dictionary>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
my_dictionary['new key'] = 'new value'
print('adding new key/value: ' + str(my_dictionary))
var = 'element to delete'
my_dictionary[var] = 'value'
print('b4 delete: ' + str(my_dictionary))
del my_dictionary[var]
print('after delte: ' + str(my_dictionary))

#clear
print('clearing my_dictionary')
my_dictionary.clear()
print(my_dictionary)

#shallow copies with dictionaries
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<shallow copies>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#shallow copy = two copies of a data structure share the same set of elements
my_dictionary = {'item': 'shirt', 'size': 'medium', "price": 50}
my_dictionary1 = my_dictionary
print('my_dictionary: '  + str(my_dictionary))
my_dictionary['size'] = 'small'
print('my_dictionary1: ' + str(my_dictionary1))