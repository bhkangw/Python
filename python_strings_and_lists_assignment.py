words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day") # print the position of the first instance of the word "day".
print words.replace("day","month") #create a new string where "day" is replaced with "month".

x = [2,54,-2,7,12,98] #print the min and max values in a list
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"] #call the first and last values of a list
print x[0] 
print x[-1] #-1 calls the last values of a list, -2 gets the second to last, etc
y = [x[0],x[-1]] #creates a new list w the first and last values
print y

x = [19,2,54,-2,7,12,98,32,10,-3,6] #Push the list created from the first half to position 0 of the list created from the second half
x.sort() #sort your list first
y = x[:len(x)/2] #split your list in half (first half)
z = x[len(x)/2:] #second half - using len/2 (length/2) and the : on the appropriate side
z.insert(0, y) #insert function lets you specify the insertion point ie. index 0
print z #prints [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]

