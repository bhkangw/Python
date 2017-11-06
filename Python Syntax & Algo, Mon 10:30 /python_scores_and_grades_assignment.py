# Assignment: Scores and Grades
# Write a function that generates ten scores between 60 and 100. 
# Each time a score is generated, your function should display what the grade is for a particular score. 
# Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

# The result should be like this:

# Scores and Grades
# Score: 87; Your grade is B
# Score: 67; Your grade is D
# Score: 95; Your grade is A
# Score: 100; Your grade is A
# Score: 75; Your grade is C
# Score: 90; Your grade is A
# Score: 89; Your grade is B
# Score: 72; Your grade is C
# Score: 60; Your grade is D
# Score: 98; Your grade is A
# End of the program. Bye!

import random # necessary to generate random numbers, must be placed anywhere before calling for random num

def givegrades():

	for i in range(0,10): # does the loop 10 times (to generate 10 random numbers)
		random_num = random.randint(60,100) # generates random num between 60 and 100
		if random_num < 70:
			print "Score:", random_num, "; Your grade is D"
		elif random_num < 80:
			print "Score:", random_num, "; Your grade is C"
		elif random_num < 90:
			print "Score:", random_num, "; Your grade is B"
		else:
			print "Score:", random_num, "; Your grade is A"
	print "End of the program. Bye!"

givegrades()