# Assignment: Car
# Create a class called  Car. 
# In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. 
# If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

# Create six different instances of the class Car. 
# In the class have a method called display_all() that returns all the information about the car as a string. 
# In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

# A sample output would be like this:

class car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if price > 10000:
			self.tax = .15
		else:
			self.tax = .12
		self.display_all()

	def display_all(self):
		print "Price: $" + str(self.price)
		print "Speed: " + str(self.speed) + "mph"
		print "Fuel: " + str(self.fuel)
		print "Mileage: " + str(self.mileage) + "mpg"
		print "Tax: " + str(self.tax)

car1 = car(50000, 100, "Full", 10)
car2 = car(20000, 80, "Not Full", 15)
car3 = car(10000, 60, "Full", 20)
car4 = car(9000, 50, "Kind of Full", 13)
car5 = car(7000, 40, "Not Full", 14)
car6 = car(5000, 30, "Not Full", 10)