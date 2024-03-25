from Tree import *


def printInOrder(root):
    '''
    Left -> Self -> Right
    '''
    if root:
        printInOrder(root.left)
        print(root.value, end=' -> ')
        printInOrder(root.right)

def printPreOrder(root):
    '''
    Self -> Left -> Right
    '''
    if root:
        print(root.value, end=' -> ')
        printPreOrder(root.left)
        printPreOrder(root.right)

def printPostOrder(root):
    '''
    Left -> Right -> Self
    '''
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.value, end=' -> ')

def printBFS(root, queue=[]):
    if root:
        print(root.value, end=' -> ')
        queue.append(root.left)
        queue.append(root.right)
        if queue:
            root=queue.pop(0)
            printBFS(root, queue)



def inOrderTraversal(root, visited=[]):
    '''
    Left -> Self -> Right
    '''
    if root:
        inOrderTraversal(root.left, visited)
        visited.append(root.value)
        inOrderTraversal(root.right, visited)
    return visited

def preOrderTraversal(root, visited=[]):
    '''
    Self -> Left -> Right
    '''
    if root:
        visited.append(root.value)
        preOrderTraversal(root.left, visited)
        preOrderTraversal(root.right, visited)
    return visited

def postOrderTraversal(root, visited=[]):
    '''
    Left -> Right -> Self
    '''
    if root:
        postOrderTraversal(root.left, visited)
        postOrderTraversal(root.right, visited)
        visited.append(root.value)
    return visited

def BFSTraversal(root, queue=[], visited=[]):
    if root:
        visited.append(root.value)
        queue.append(root.left)
        queue.append(root.right)
        if queue:
            root=queue.pop(0)
            BFSTraversal(root, queue, visited)
    return visited




root=Tree(1)
insert(root, 2)
insert(root, 3)
insert(root, 4)
insert(root, 5)
insert(root, 6)
insert(root, 7)


printInOrder(root)
print()
printPreOrder(root)
print()
printPostOrder(root)
print()
printBFS(root)
print()




print(inOrderTraversal(root))
print(preOrderTraversal(root))
print(postOrderTraversal(root))
print(BFSTraversal(root))