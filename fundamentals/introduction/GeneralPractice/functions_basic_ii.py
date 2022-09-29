def countdown(a):
    countdown_list = []
    while a >= 0:
        countdown_list.append(a)
        a = a-1
    print(countdown_list)
countdown(5)

def print_return(list):
    print(list[0])
    return(list[1])
print(print_return([5,3]))

def firstpluslength(list):
    sumof = list[0] + len(list)
    print(sumof)
firstpluslength([150,20,30,10])

def values_greater_than_second(list):
    if len(list) < 2: #if the length of the list is less than 2
        return False #Return false and end function
    output = [] #sets a list named output
    for i in range(0,len(list)): #i starts at 0 and goes through to the length of the list
        if list[i] > list[1]: #if list[i] which will be a value going from 0 to the end of the list is less than the 2nd value of the list
            output.append(list[i]) #then the number gets added to the list and it checks the next number
    print(len(output)) #prints the length of the output 
    return output #gives the output list

print(values_greater_than_second([10,30,40,24,12,55]))

def this_length_that_value(a,b): # defines the function
    output = [] #creates an output list
    x = 0 #sets x to 0, x will be our counter to print more 
    while (x < a): #while x is less than a
        output.append(b) #it adds b to the list
        x = x+1 #adds 1 to x which is the counter and then loops back
    print(len(output)) #gives the length of the list
    return(output) #returns the list
print(this_length_that_value(30,1))
## I did thislengththatvalue without looking at anything. good work me
