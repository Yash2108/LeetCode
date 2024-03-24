# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited=[]
        counter=0
        while head!=None:
            if head not in visited:
                visited.append(head)
                counter+=1
                head=head.next
            else:
                return True
        return False