#1
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)
print('')

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}]
students[0]['last_name'] = 'Bryant'
print(students)
print('')

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
print('')

z = [ {'x': 10, 'y': 20}]
z[0]['y'] = 30
print(z)
print('')

#2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'}, # index 0
        {'first_name' : 'John', 'last_name' : 'Rosales'}, # index 1
        {'first_name' : 'Mark', 'last_name' : 'Guillen'}, # index 2
        {'first_name' : 'KB', 'last_name' : 'Tonel'} # index 3
    ]

def iterateDictionary(students):
    for i in range(len(students)):
        print('first_name -',students[i]['first_name'], ',' ,'last_name -',students[i]['last_name'])

print(iterateDictionary(students))
print('')

#3
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])

print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students))
print('')


#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'], 
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict): 
    for key, val in some_dict.items():
        print(len(val), key)
        for i in range(len(val)):
            print(val[i])
        print('')

print(printInfo(dojo))








