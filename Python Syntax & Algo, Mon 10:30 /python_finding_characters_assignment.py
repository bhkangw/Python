# Assignment: Find Characters
# Write a program that takes a list of strings and a string containing a single character, 
# and prints a new list of all the strings containing that character.

# Here's an example:

# # input
list = ['hello','world','my','name','is','Anna']
char = 'o'

# # output
# new_list = ['hello','world']

def find_characters(list,char):
	
	new_list = []

	for value in list:
		if char in value:
			new_list.append(value)
	
	print new_list

find_characters(list, char)



# CD different solution using a different type of for loop & .find(char) rather than: if "char" in ___
def find_character(list, char):

    new_list = []

    for i in range(0, len(list)): # Question: what's the difference between this for loop and mine above?
        if list[i].find(char) != -1:
            new_list.append(list[i])

    print new_list

find_character(list, char)