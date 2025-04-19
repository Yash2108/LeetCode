"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping={}

        new_head=Node(0)
        new_node=Node(0)
        new_head.next=new_node
        head_copy=head

        while head:
            node=Node(head.val)
            mapping[head]=node
            new_node.next=node
            new_node=new_node.next
            head=head.next
            
        while head_copy:
            if head_copy.random:
                mapping[head_copy].random=mapping[head_copy.random]
            head_copy=head_copy.next
        return new_head.next.next