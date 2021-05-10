#1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
#def countdown(x):
#    for i in range (x, -1,-1):
#        print(i)
#    return i
#countdown(5)
#countdown(9)
#countdown(33)

#2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
#def printReturn(x,y):
#    print(x)
#    return y
#printReturn(3,6)
#print(printReturn(3,6))


#3.First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#def firstLength(x):
#    return len(x) + x[0]
#print(firstLength([3,6,9,12]))
#print(firstLength([2,4,6,8]))

#4.Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False.
#x = 0
#newArr = []
#def valueGreater(a):
#    for x in range (0, len(a), 1):
#        if len(a) < 3:
#            print(False)
#        elif a[x] >= a[2]:
#            newArr.append(a[x])
#    print(newArr)
#valueGreater([2,7,36,5,27])
#valueGreater([2,7,3,5,0,1,27])
#valueGreater([2,7])


#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, 
# and whose values are all the given value.
newArr = []
def thisThat(x,y):
    for i in range (0, x, 1):
        newArr.append(y)
    print(newArr)
#thisThat(3,7)
thisThat(5,3)