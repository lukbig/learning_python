#inheritance
print('<<<<<<<<<<<<<<<<<<<<<inheritance>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

class Vehicle:

	# shared variable/ static variable
	no_of_vehicles = 0

	def __init__(self, VIN, weight, manufacturer):
		self.__vin_number = VIN
		self.__weight = weight
		self.__manufacturer = manufacturer
		Vehicle.no_of_vehicles += 1

	#defining destructor
	def __del__(self):
		Vehicle.no_of_vehicles -= 1

	def getWeight(self):
		return self.__weight
	def getManufacturer(self):
		return self.__manufacturer
	def getVehicleType(self):
		pass
	def getVinNumber(self):
		return self.__vin_number		

class Car(Vehicle):
	"""docstring for Car"Vehicle"""
	def __init__(self, VIN, weight, manufacturer, seats):
		super(Car, self).__init__(VIN, weight, manufacturer)
		self.__seats = seats

	def getSeats(self):
		return self.__seats
	def getVehicleType(self):
		return 'car'


class Truck(Vehicle):
	"""docstring for Car"Vehicle"""
	def __init__(self, VIN, weight, manufacturer, capacity):
		super().__init__(VIN, weight, manufacturer)
		self.__capacity = capacity

	def getCapacity(self):
		return self.__capacity
	def getVehicleType(self):
		return 'truck'

a = Car('ABC1', 1000, "BMW", 4)
b = Truck('BC2', 2000, 'MAN', 10000)

for v in [a,b]:
	print('vehicle type: ' + v.getVehicleType() + ' manufacturer: ' + v.getManufacturer())

print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<static variables>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('number of vehicles: ' + str(Vehicle.no_of_vehicles))
c = Car('ag', 100, "Audi", 5)
print('number of vehicles after audi creation: ' + str(Vehicle.no_of_vehicles))
del c
print('number of vehicles after audi deletion: ' + str(Vehicle.no_of_vehicles))