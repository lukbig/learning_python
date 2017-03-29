#open(filename, access, buffering)
#reading whole fle
print('<<<<<<<<<<<<<<<<<<<<<<reading whole file>>>>>>>>>>>>>>>>>>>>>>>>>>')
file = open("wood.txt", "r")
#reading whole file
print(file.read())
file.close()

#reading 4 bytes
print('<<<<<<<<<<<<<<<<<<<<<<reading 4 bytes>>>>>>>>>>>>>>>>>>>>>>>>>>')
file = open("wood.txt", "r")
print(file.read(4))
#file.tell() - current postion of the pointer
print('current position of the pointer is {0}'.format(file.tell()))
print(file.read(2))
print('current position of the pointer is {0}'.format(file.tell()))
#file.seek() - move pointer
file.seek(2)
#pointer moved to 2nd position
print('current position of the pointer is {0}'.format(file.tell()))
file.close()

#itering threw file
file = open("wood.txt", "r")
i = 1
for line in file:
	print('line number {0}: {1}'.format(i, line), end = "")
	i = i + 1
print('')

#file properties
print("file name: " + file.name)
print("is closed: " + str(file.closed))
print("mode: " + file.mode)

file.close()

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<writing to file>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
file = open("wood1.txt", "w+")
file.write("hello file, i am string")
#go to start of file
file.seek(0)
print(file.read())
file.close()