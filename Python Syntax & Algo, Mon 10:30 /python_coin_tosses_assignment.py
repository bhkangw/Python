# Assignment: Coin Tosses
# Write a function that simulates tossing a coin 5,000 times. 
# Your function should print how many times the head/tail appears.

# Sample output should be like the following:

# Starting the program...
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ...
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
# Ending the program, thank you!

# Hint: Use the python built-in round function to convert that floating point number into an integer

# x = .23945593
# y = .798839238
# x_rounded = round(x) = 0
# y_rounded = round(y) = 1

import random

def coin_toss(toss):
	headcount = 0
	tailcount = 0
	coinside = ""
	for i in range(1,toss+1): # range up to toss = number of tosses. The +1 makes it so if you input 5000 it flips 5000 times, not 4999
		random_num = random.randint(0,1) # gives two options of the random number, 0 or 1 aka heads or tails
		if random_num == 0:
			coinside = "head"
			headcount = headcount + 1
			print "Attempt #", i, ": Throwing a coin... it's a", coinside, "! ... Got ", headcount, "head(s) so far and", tailcount, "tail(s) so far"
		elif random_num == 1:
			coinside = "tail"
			tailcount = tailcount + 1
			print "Attempt #", i, ": Throwing a coin... it's a", coinside, "! ... Got ", headcount, "head(s) so far and", tailcount, "tail(s) so far"
coin_toss(5000)