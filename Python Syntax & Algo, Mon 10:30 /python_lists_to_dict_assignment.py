# Assignment: Making Dictionaries
# Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. 
# Assume the lists will be of equal length.

# Your first function will take in two lists containing some strings. Here are two example lists:

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "pony"]

# Here's some help starting your function.

# def make_dict(arr1, arr2):
#   new_dict = {}
#   # your code here
#   return new_dict

def make_dict(arr1,arr2):
	
		new_list = zip(arr1,arr2)
		new_dict =  dict(new_list)
		print new_dict

make_dict(name,favorite_animal)

# Hacker Challenge:
# If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values.

# def make_dict(arr1,arr2):

# 	if len(arr2) > len(arr1):
# 		new_list = zip(arr2,arr1)
# 		new_dict =  dict(new_list)
# 		print new_dict
# 	else:
# 		new_list = zip(arr1,arr2)
# 		new_dict =  dict(new_list)
# 		print new_dict

# make_dict(name,favorite_animal)