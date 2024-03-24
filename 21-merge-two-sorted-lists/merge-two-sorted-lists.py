# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # def printLL(self, ll):
    #     while ll:
    #         print(ll.val, '-> ', end='')
    #         ll=ll.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return
        elif list1==None:
            return list2
        elif list2==None:
            return list1
        elif list1.val>list2.val:
            curr=list2
            list2=list2.next
        else:
            curr=list1
            list1=list1.next
        head=curr

        while list1!=None or list2!=None:
            # self.printLL(head)
            # print()
            # self.printLL(list1)
            # print()
            # self.printLL(list2)
            # print()
            # print()
            # print(curr, list1, list2)
            if list1==None:
                curr.next=list2
                # print(list1)
                return head
            elif list2==None:
                curr.next=list1
                # print(list2)
                return head
            if list1.val>list2.val:
                curr.next=list2
                list2=list2.next
            else:
                curr.next=list1
                list1=list1.next
            curr=curr.next
        self.printLL(head)
        return head