# Reading the maze dimensions and layout from the txt file 
with open(r'Python\Course15.1.txt') as r: 
    input = r.read().split('15')
    #print(len(input))
courses = []
modules = []

for i in input: 
    courses.append(i.split('\n'))
print(courses)
k = 0
for j in courses: 
    for line in j: 
        if 'Undergrad' in line:  
            print (True)
            modules.append(j[0][5:])
            k += 1 

print(modules)
print(k)