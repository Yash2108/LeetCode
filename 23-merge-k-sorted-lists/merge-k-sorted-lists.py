# Definition for singly-linked list.
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

        initial_node=ListNode()
        new_node=initial_node
        while lists:
            only_vals=[ls.val for ls in lists]
            minimum_idx=only_vals.index(min(only_vals))
            new_node.next = ListNode(val=lists[minimum_idx].val)
            new_node=new_node.next
            if lists[minimum_idx].next:
                lists[minimum_idx]=lists[minimum_idx].next
            else:
                lists.pop(minimum_idx)
        
        return initial_node.next
