# Assignment: Compare Lists
# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

# Your program should be able to accept and compare two lists: list_one and list_two. 
# If both lists are identical print "The lists are the same". 
# If they are not identical print "The lists are not the same." 
# Try the following test cases for lists one and two:

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']

def compare_lists(list1,list2):

	if list_one == list_two: # don't overthink it! To check if lists are identical, literally check if they equals each other!
		print "The lists are the same."

	else:
		print "The lists are not the same."

compare_lists(list_one,list_two)