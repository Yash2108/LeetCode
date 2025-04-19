# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=current=ListNode()
        carryover=0

        while l1 and l2:
            current.next=ListNode()
            current=current.next
            current.val = l1.val + l2.val + carryover
            if current.val>9:
                current.val%=10
                carryover=1
            else:
                carryover=0
            l1=l1.next
            l2=l2.next
        
        while l1:
            current.next=ListNode()
            current=current.next
            current.val = l1.val + carryover
            if current.val>9:
                current.val%=10
                carryover=1
            else:
                carryover=0
            l1=l1.next
        
        while l2:
            current.next=ListNode()
            current=current.next
            current.val = l2.val + carryover
            if current.val>9:
                current.val%=10
                carryover=1
            else:
                carryover=0
            l2=l2.next
        
        if carryover==1:
            current.next=ListNode()
            current=current.next
            current.val=1

        return head.next
