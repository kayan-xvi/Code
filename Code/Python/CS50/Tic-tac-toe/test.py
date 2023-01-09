import sys

'''
from collections import Counter

z = ['+','-','-']

print(Counter(z))
possible = ['|','-','+']
for i in possible:
    print(i)
    if Counter(z)[i] > 1 : 
        print('hu')
        '''
#if 'r' == ('t' or 'r' or 'p'):
    #print(True)
'''
class hello: 
    def __init__(self): 
        self.hi = False 

def Function(): 
    yueb.hi = True 

yueb = hello() 
Function() 
print(yueb.hi)
'''

names = ['example0', 'example1', 'example2', 'example3']
class Count: 
    def __init__(self):
        self.number = 0


class Class1: 
    def __init__(self): 
        self.status = True 
        self.name = 'example0'
    def newName(self): 
        name = self # 'example' + str(int(self.name[7]) + 1)
        print(name)
        return(name)
    @classmethod
    def reproduce(cls): 
        return cls()

# array = ['example1', 'example2']
array = []
# print(type(array[0]))
variable = Count()
example = Class1()

def newInstances(): 
    for i in range(50): 
        array.append('example' + str(i))
        array[i] = example.reproduce()
        array[i].name = 'example' + str(i)
        array[i].newName()
    # print(array)
    return array 

array = newInstances()
array[15].status = False
print(array[15].status)
print(array[43].name)

# print(type(array[0]))
# print(array[0].name)
# print(type(array[1]))
# print(array[1].name)


# example1 = example0.reproduce()
# example1.newName()
# vars(names[2]) = 0
# exec(f'example{example1.newName} = example0.reproduce()')
# example0 = Class1()
# example1 = example0.reproduce()
# exec(f'{names[2]} = example0.reproduce')
# print(example0)
# print(example1)
# print(example2)
# print(type(example0))
# print(type(example1))
# print(type(example2))
# example1.status = False
# print(example1.status)
#exec(f'{names[3]} = example2.reproduce')
#print(example3)