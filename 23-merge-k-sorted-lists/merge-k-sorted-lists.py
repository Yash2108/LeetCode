# Definition for singly-linked list.
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while None in lists:
            lists.pop(lists.index(None))
        if len(lists)==0:
            return 

        heap = []
        heapq.heapify(heap)
        for ls in lists:
            while ls:
                heapq.heappush(heap, ls.val)
                ls=ls.next

        initial_node=ListNode()
        new_node=initial_node
        while heap:
            new_node.next=ListNode(val=heapq.heappop(heap))
            new_node=new_node.next
        return initial_node.next
