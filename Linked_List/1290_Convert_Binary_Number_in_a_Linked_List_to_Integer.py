# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = []
        while head:
            result.append(str(head.val))
            head = head.next
        
        outcome = "".join(result)
        return int(outcome,base =2)
            
