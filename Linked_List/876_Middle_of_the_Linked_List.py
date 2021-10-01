# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        n = 0
        tmp = head
        while tmp!=None:
            n +=1
            tmp = tmp.next
            
        idx = int(n/2)
        
        while idx:
            head = head.next
            idx -=1
        return head
