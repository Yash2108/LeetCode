from Tree import Tree


root=Tree(1)
root.left=Tree(2)
root.right=Tree(3)
root.left.left=Tree(4)
root.left.right=Tree(5  )
root.right.left=Tree(6)
root.right.right=Tree(7)

def inOrderTraversal(root):
    '''
    Left -> Self -> Right
    '''
    if root:
        inOrderTraversal(root.left)
        print(root.value, end=' -> ')
        inOrderTraversal(root.right)

def preOrderTraversal(root):
    '''
    Self -> Left -> Right
    '''
    if root:
        print(root.value, end=' -> ')
        inOrderTraversal(root.left)
        inOrderTraversal(root.right)

def postOrderTraversal(root):
    '''
    Left -> Right -> Self
    '''
    if root:
        inOrderTraversal(root.left)
        inOrderTraversal(root.right)
        print(root.value, end=' -> ')

def BFS(root, queue=[]):
    if root:
        print(root.value, end=' -> ')
        # visited.append(root.value)
        queue.append(root.left)
        queue.append(root.right)
        if queue:
            root=queue.pop(0)
            BFS(root, queue)

inOrderTraversal(root)
print()
preOrderTraversal(root)
print()
postOrderTraversal(root)
print()
BFS(root)
