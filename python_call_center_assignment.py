# Assignment: Call Center
# You're creating a program for a call center. 
# Every time a call comes in you need a way to track that call. 
# One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.

# You will create two classes. One class should be Call, the other CallCenter.

# Call Class:

# Create your call class with an init method. Each instance of Call() should have:

# Attributes:
# unique id
# caller name
# caller phone number
# time of call
# reason for call

# Methods:
# display: that prints all Call attributes.
from datetime import datetime

class Call(object):
	call_number = 1
	def __init__(self, name, phonenum, reason):
		self.uniqueid = Call.call_number
		self.name = name
		self.phonenum = phonenum
		self.time = datetime.now()
		self.reason = reason
		Call.call_number +=1

	def display(self):
		print "ID: " + str(self.uniqueid)
		print "Name: " + str(self.name)
		print "Phone Number: " + str(self.phonenum)
		print "Time of Call: " + str(self.time)
		print "Reason for Call: " + str(self.reason)
		return self

firstcall = Call("Brian", 425, "whine")
# firstcall.display()
secondcall = Call("Me", 425, "whine")
# firstcall.display()

class CallCenter(object):
	def __init__(self):
		self.listofcalls = []
		self.queue = self.get_queue_size()

	def get_queue_size(self):
		# print self.listofcalls
		return len(self.listofcalls)
		return self

	def add(self, new_call):
		self.listofcalls.append(new_call)
		return self

	def remove(self):
		listofcalls.pop(0)
		return self

	def info(self):
		for call in self.listofcalls:
			call.display_info()
		print self.queue
		return self

center1 = CallCenter()
print center1.add(firstcall).get_queue_size()

center2 = CallCenter()
print center2.add(secondcall).get_queue_size()






