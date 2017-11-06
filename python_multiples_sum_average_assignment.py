for count in range(1,1000,2): # print  all odd numbers from 1-1000
	print count

for count in range(5,1000001,5): # print  all multiples of 5 from 5-1000000
	print count

a = [1, 2, 5, 10, 255, 3] # prints the sum of all values of a list
sum = sum(a)
print sum

# SAME AS ABOVE (using a for loop)
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print sum


a = [1, 2, 5, 10, 255, 3] # prints the average of all the values of a list
sum = sum(a)
avg = sum/len(a)
print avg
