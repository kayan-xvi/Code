# Reading the maze dimensions and layout from the txt file 
with open(r'Python\Course15.txt') as r: 
    input = r.read().split('\n15.')
    #print(len(input))
modules = []
courses = []

for i in input: 
    courses.append(i.split('\n'))
#print(courses)

k = 0
for j in courses: 
    for line in j: 
        if len(line) >= 1: 
            #print(line)
            if 'U (' in line:  
                #print (True)
                modules.append(j[0][5:])
                k += 1 

print(modules)
print(f'{k} == {len(modules)}') 
