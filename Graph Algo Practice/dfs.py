from random import random
from Node import *

random_num=(random()*100)//1
node1 = Node(random_num, 10)
node2 = Node(random_num, 20)
node3 = Node(random_num, 30)
node4 = Node(random_num, 40)
node5 = Node(random_num, 50)
node6 = Node(random_num, 60)
node1.addEdge(node2)
node2.addEdge(node4)
node1.addEdge(node3)
node4.addEdge(node3)
node5.addEdge(node3)
node5.addEdge(node4)

def dfs(source, destination, visited):
    if source in visited:
        return False
    visited.append(source)
    if source==destination:
        return True
    
    for node in source.adjacent:
        if dfs(node, destination, visited):
            return True
        
    return False



print(dfs(node1, node6, []))