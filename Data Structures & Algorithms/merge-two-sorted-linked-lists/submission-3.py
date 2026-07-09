# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = list1, list2
        res, curr = ListNode(), ListNode()
        curr = res
        while n1 or n2:
            val1 = n1.val if n1 else float('infinity')
            val2 = n2.val if n2 else float('infinity')
            if val1 < val2:
                curr.next = n1
                n1 = n1.next
            else:
                curr.next = n2
                n2 = n2.next
            curr = curr.next
        return res.next





