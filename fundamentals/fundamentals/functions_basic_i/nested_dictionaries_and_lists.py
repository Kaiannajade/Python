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

#TODO: change the value 10 in x to 15,once you are done, x should now be [[5,2,3],[15,8,9]]
x[1][0] = 15:
print(x)

#TODO:  change the last name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = "Bryant"
print(students)

#TODO: In the sports directory change 'Messi' to 'Andres'
sports_directory['soccer'][0]='Andres'
print(sports_directory[soccer])

#TODO: chamge the value 20 in z to 30
z[0]['y']= 30
print(z)


#! Iterate through a list of dictionaries
# create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and printseach key amd the associated value. For example given the following value:

 def iterate_dictionary(list):
    for i in range(0,len(list)-1):
        output:""
        for key,val in list [i].items():
            output += f" {key} - {val}"
            print(output)
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel


#TODO:  get values from list of dictionaries!
# create a function iterateDictionary2(key_name, some_list)that given a list of dictionaries and a key name, the function prints the value stored,in that key for each dictionary.  For example iterateDictionary2('first_name', students) should output:
 
Michael
John
Mark
KB

def iterate_dictionary2(key_name,list):
    for i in range(0,len(list)):
        for key,val in list[i].items():
            if key == "key_name":
                print(val)
                iterate_dictionary2('first_name',students)
                iterate_dictionary2('last_name',students)

Jordan
Rosales
Guillen
Tonel


#TODO: Iterate through a Dictionary with List Values

def print_info(dict):
    for key, val in dict.items():
        print("----------")
        print(f"{len(val)} {key.upper()}")
        print_info(dojo)
        for i in range (0,len(val)):
            print(val[i])
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon




