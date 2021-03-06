# Assignment: Product
# The owner of a store wants a program to track products. Create a product class to fill the following requirements.

# Attributes:

#  Price
#  Item Name
#  Weight
#  Brand
#  Status: default "for sale"

# Methods:

#  Sell: changes status to "sold"
#  Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
#  Return: takes reason for return as a parameter and changes status accordingly. 
#		If the item is being returned because it is defective change status to defective and change price to 0. 
# 		If it is being returned in the box, like new mark it as for sale. 
# 		If the box has been opened set status to used and apply a 20% discount.
#  Display Info: show all product details.

# Every method that doesn't have to return something should return self so methods can be chained

class Product(object):
	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "For Sale"
		self.display_info()

	def sell(self):
		self.status = "Sold"
		return self

	def add_tax(self, tax):
		self.price = self.price*tax
		return self

	def return_item(self, reason):
		if(reason == "efective"):
			self.status = "Defective"
			self.price = 0
		elif(reason == "in the box" or "like new"):
			self.status = "For Sale"
		elif(reason == "box opened" or "opened"):
			self.status = "Used"
			self.price = self.price*.80
		return self

	def display_info(self):
		print "Price: $" + str(self.price)
		print "Item Name: " + str(self.item_name)
		print "Weight: " + str(self.weight) + " lbs"
		print "Brand: " + str(self.brand)
		print "Status: " + str(self.status)

product1 = Product(20, "Book", 5, "Adidas")
