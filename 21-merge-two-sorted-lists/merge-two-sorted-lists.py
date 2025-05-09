# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list=head=ListNode()

        if list1==None:
            return list2
        if list2==None:
            return list1
                
        while list1!=None and list2!=None:

            if list1.val>list2.val:
                new_list.next=list2
                list2=list2.next
            else:
                new_list.next=list1
                list1=list1.next
            new_list=new_list.next

        new_list.next = list1 or list2


        return head.next