x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]
print(x[1][0])
x[1][0] = 15
print(x[1][0])
sports_directory["basketball"][1] = "Bryant"
print(sports_directory["basketball"][1])
sports_directory["soccer"][0] = "Andres"
print(sports_directory["soccer"][0])
print("----")
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iteratedirectory(some_list):
    for i in (some_list):
        print(f'first_name - {i["first_name"]}, last_name - {i["last_name"]}')

iteratedirectory(students)

def iteratedirectory2(key_name, some_list):
    for i in (some_list):
        if key_name == 'first_name':
            print(f"{i['first_name']}")
        if key_name == 'last_name':
            print(f"{i['last_name']}")
            
iteratedirectory2('first_name', students)
iteratedirectory2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#print(dojo['instructors'][7])
#print(dojo)

def printinfo(another_list):
    for item in another_list:
        print(f"{len(another_list[item])} {item.upper()}")
        for i in range(len(another_list[item])):
            print(another_list[item][i])

printinfo(dojo)