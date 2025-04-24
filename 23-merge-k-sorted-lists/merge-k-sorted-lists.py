from heapq import heapify, heappush, heappop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        heapify(heap)

        for ls in lists:
            while ls:
                heappush(heap, ls.val)
                ls=ls.next
        result=ListNode(None, None)
        head=result
        while heap:
            new_node = ListNode(heappop(heap))
            head.next = new_node
            head = head.next
        return result.next