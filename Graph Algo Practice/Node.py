class Node:
    def __init__(self, node_id, key) -> None:
        self.adjacent=[]
        self.id=node_id
        self.value=key

    def addEdge(self, node):
        self.adjacent.append(node)
        node.adjacent.append(self)