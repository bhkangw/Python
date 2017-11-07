# Assignment: MathDojo
# HINT: To do this exercise, you will probably have to use 'return self'. 
# If the method returns itself (an instance of itself), we can chain methods.

# PART I
# Create a Python class called MathDojo that has the methods add and subtract. 
# Have these 2 functions take at least 1 parameter.

# Then create a new instance called md. It should be able to do the following task:

	# md.add(2).add(2,5).subtract(3,2).result

# which should perform 0+2+(2+5)-(3+2) and return 4.

class MathDojo(object):
	def __init__(self):
		self.result = 0 # starts at 0 so we give it the only attribute of 0

	def add(self,*x): # * specifies multiple arguments can be passed.. "at least one"
		for t in x: # need to add a for loop so that the addition is cycled though the multiple values given as arguments.
			self.result += t # this adds each value in the tuple ie for (2,5) - first 2 then 5
		return self

	def subtract(self,*x):
		for t in x:
			self.result -= t
		return self

md = MathDojo() # creates the instance by calling the Class, no perameters necessary
print md.add(2).add(2,5).subtract(3,2).result

# PART II
# Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with any number of values passed into the list. 
# It should now be able to perform the following tasks:

# md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result

# should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.

class MathDojo(object):
	def __init__(self):
		self.result = 0

	def add(self,*x):
		for t in x: # for every value in the given argument
			if type(t) == list or type(t) ==tuple: # check to see if type is list or tuple, is so:
				for i in t: # cycle through each value and add to result on next line
					self.result += i
			else:
				self.result += t # if NOT a list or tuple, just add the value straight to the result
		return self

	def subtract(self,*x):
		for t in x:
			if type(t) == list or type(t) == tuple:
				for i in t:
					self.result -= i
			else:
				self.result -= t
		return self

md = MathDojo()
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result






