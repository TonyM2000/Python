#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# Guessing this outputs 5

# #2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# So the first parameter isnt defined so I think it just prints 5. Ok it actually just gives an error since its
# partially undefined


# #3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#I think this will return 10 since at first it returns 5 but then returns 10 ok it actually returns 5- 
#RETURN IS ABSOLUTE SO A SECOND RETURN DOESNT MATTER


# #4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#Return is the last thing that happens, so print won't run

# #5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# I think this will just print 5
#It also printed none since great lakes has nothing inside


# #6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#I think this will print 8
# It doesn't print 8, because the function prints rather than returns. If I swap print(b+c) to return(B+C) it works


# #7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# I think this returns 2,5 ok it actually returns 25 which makes sense since it is putting 2 strings together


# #8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# This should return 10. It prints 100 then 10 since it has print(b)


# #9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Prints 7 then prints 14 then prints 21 

# #10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#So this is pretty simple it'll return 8 because return only works once


# #11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#prints 500 then 500 then 300 then 300. Ok so it does 500,500,300,500. this is because b is only 300 in foobar

# #12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


# #13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#prints 500,500,300,300

# #14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
##prints 1 3 2

# #15
def foo():
    print(1) #1st
    x = bar() #2nd
    print(x) #4th
    return 10
def bar():
    print(3) #3rd
    return 5 #4th
y = foo()
print(y)
#1,5,3,10 its 1