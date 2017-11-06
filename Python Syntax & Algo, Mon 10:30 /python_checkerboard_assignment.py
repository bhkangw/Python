# Assignment: Checkerboard
# Write a program that prints a 'checkerboard' pattern to the console.

# Your program should require no input and produce console output that looks like so:

# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *

# Each star or space represents a square. 
# On a traditional checkerboard you'll see alternating squares of red or black. 
# In our case we will alternate stars and spaces. The goal is to repeat a process several times. 
# This should make you think of looping.

def create_checkerboard():

	line_one = "* " * 4
	line_two = " *" * 4

	for count in range(0,5): # uses a range so it repeats 5 times
		print line_one
		print line_two

create_checkerboard()


def checkerboard(): # CD different solution 

    for i in range(0,10):
       
        if i%2 == 0:
            print "* " * 5
        else:
            print " *" * 5

checkerboard()