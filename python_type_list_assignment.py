# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type. 
# If the item is a string, concatenate it onto a new string. 
# If it is a number, add it to a running sum. 
# At the end of your program print the string, the number and an analysis of what the list contains. 
# If it contains only one type, print that type, otherwise, print 'mixed'.

list1 = ['magical unicorns',19,'hello',98.98,'world']
list2 = [2,3,1,7,4,12]
list3 = ['magical','unicorns']

def list_type(list):

	newstr = ""
	sum = 0

	for value in list: # for loop goes through the values and determines the type
		if isinstance(value,int) or isinstance(value,float): # if value is a int/float, add to sum
			sum = sum + value
		elif isinstance(value,str): # if value is a string, add to newstr
			newstr = newstr + " " + value

	if newstr and sum: # if result contains both newstr and sum, we know it's mixed
		print "The list you entered is of mixed type"
		print "String:", newstr
		print "Sum:", sum

	elif newstr: # if result contains only newstr, we know it's a string type only
		print "The list you entered is of string type"
		print "String:", newstr

	else: # anything else, we know it only contains a sum therefore it's of an integer type
		print "The list you entered is of integer type"
		print "Sum:", sum

list_type(list1)