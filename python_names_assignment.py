# Assignment: Names
# Write the following function.

# Part I
# Given the following list:

students = [
     {'first_name' : 'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# Create a program that outputs:

# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

def combine_names(list):
	for i in students:
			print i['first_name'], i['last_name']
combine_names(students)

# Part II
# Now, given the following dictionary:

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# Create a program that prints the following format (including number of characters in each combined name):

# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13


def combine_names2(list): # first way of solving
	for type in users:
		counter = 0
		print type
		for i in users[type]:
			counter = counter + 1
			print counter, "-", i['first_name'], i['last_name'],"-", len(i['first_name']) + len(i['last_name'])
		
combine_names2(users)


def show_all(users): # similar way of solving expect used variables for 'cleaner' code
    for title in users: # first step is to loop through the dictionary - for ___ in users
        counter = 0 # defines the counter var
        print title # prints either student or instructor (the name of the nested object)
        for name in users[title]: # second step is to loop through the nested object
            counter += 1 # counts up within the nested object ie. students OR instructors
            first_name = name['first_name'].upper()
            last_name = name['last_name'].upper()
            length = len(first_name) + len(last_name)
            print counter, "-", first_name, last_name, "-", length 
            # print "{} - {} {} - {}".format(counter, first_name, last_name, length) # different way of formatting the above print

show_all(users)