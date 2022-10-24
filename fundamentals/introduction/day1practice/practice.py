# Practice Challenge: Correct the errors!
first_name = "Alana "
last_name = "Da Silva"
age = 36
profession = "Software Developer"
years_experience = 5

greeting = "Hello my name is "+ first_name + last_name

print(greeting) 
# Desired output: Hello my name is Alana Da Silva

print(f"I am {age} years old") 
# Desired output: I am 36 years old

name = "Zen"
print("My name is", name)

name = "Zen"
print("My name is " + name)

print(f"I work as a {profession}.".format(profession))
# Desired output: I work as a Software Developer.

exp_string = "I have worked in the field for {} years."
print(exp_string.format(years_experience))
# Desired output: I have worked in the field for 5 years.

print("I started in the field when I was ", int(age - years_experience)," years old.")
# Desired output: I started in the field when I was 31 years old.

# Challenge 1:
#   Fill in the missing code for the full_name function.
#   Be sure to add the 2 parameters (and name them appropriately)
#   Return the full name to get the desired output!

def full_name(firstname,lastname):
    print(firstname,lastname)

name1 = full_name("Eddie", "Aikau")
name1