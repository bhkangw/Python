# Assignment: Making and Reading from Dictionaries
# Create a dictionary containing some information about yourself. 
# The keys should include name, age, country of birth, favorite language.

# Write a function that will print something like the following as it executes:

# My name is Anna
# My age is 101
# My country of birth is The United States
# My favorite language is Python

# There are two steps to this process, building a dictionary and then gathering all the data from it. 
# Write a function that can take in and print out any dictionary keys and values.

bio = {
	"name": "Brian",
	"age": 27,
	"country of birth": "The United States",
	"favorite language": "Python",
}

def give_bio(obj):
	for key,data in obj.iteritems():
		print "My", key, "is", data
give_bio(bio)


# for reference, how to extract only the keys or only the values
def give_bio(obj):
	for key in obj.iterkeys():
		print key
give_bio(bio)

def give_bio(obj):
	for values in obj.itervalues():
		print values
give_bio(bio)