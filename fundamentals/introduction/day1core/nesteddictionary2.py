x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x[0],x[1])
students[0]["last_name"]="Bryant"
print(students[0]["last_name"])
sports_directory['soccer'][0]="Andres"
print(sports_directory)
z[0]['y']=30
#------\
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

def iteratedirectory2(some_list):
    for i in (some_list):
            print(f"{i['first_name']}")
    for i in (some_list):
            print(f"{i['last_name']}")
            
iteratedirectory2(students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#print(dojo['instructors'][7])
#print(dojo)

def printinfo(another_list):
    for item in another_list:
        print(f"{len(another_list[item])} {item.upper()}")
        for i in another_list[item]:
            print(i)

printinfo(dojo)
