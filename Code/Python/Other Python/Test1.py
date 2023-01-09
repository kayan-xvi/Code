class Node: 
    def __init__ (self, name, information):
        self.information = {} 
        self.information[name] = information 

nodes = Node('node0',{'x':'hi', 'y':3})
nodes.information['node1'] = {'x':'hey', 'y':2}

def function(): 
    i = 2
    f = {'x':'hello', 'y':5}
    exec( f'''nodes.information['node{i}'] = {f}''')
    print(nodes.information)


#function() 

dction = {'a' : 1}

print(dction.keys())
print(type(list(dction.keys())[0]))