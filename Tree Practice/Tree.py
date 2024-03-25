class Tree:
    def __init__(self, key) -> None:
        self.left=None
        self.right=None
        self.value=key

def insert(root, key):
    if not root:
        return Tree(key)
    
    queue = [root]

    while queue:
        temp=queue.pop(0)
        if not temp.left:
            temp.left = Tree(key)
            break
        else:
            queue.append(temp.left)
        
        if not temp.right:
            temp.right = Tree(key)
            break
        else:
            queue.append(temp.right)
    
    return root
    
