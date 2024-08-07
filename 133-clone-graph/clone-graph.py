# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node==[] or node==[[]] or node==None:
            return node
        visited=set()

        def dfs(v, visited):
            if v in visited:
                return False

            visited.add(v)
            if v.neighbors:
                for neighbor in v.neighbors:
                    dfs(neighbor, visited)

        dfs(node, visited)
        adj_graph=[[] for _ in range(len(visited))]

        visited=set()
        toVisit=[node]

        while toVisit:
            current_node=toVisit.pop(0)
            if current_node in visited:
                continue
            visited.add(current_node)
            for neighbor in current_node.neighbors:
                adj_graph[current_node.val-1].append(neighbor.val)
                toVisit.append(neighbor)
        nodes=[Node(val=idx+1) for idx in range(len(visited))]
        for idx, row in enumerate(adj_graph):
            for val in row:
                nodes[idx].neighbors.append(nodes[val-1])


        return nodes[0]
