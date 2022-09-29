def multiply(num_list,num): # Defines function
    for x in range(len(num_list)): #Says "While x is in the range of 4" do the following
        num_list[x] *= num #take x and multiply it by num. x is at first 0 so it hits 2, then 1 so it hits 4 and so forth
    return num_list 
a = [2,4,10,16]
b = multiply(a,5)
print(b)

