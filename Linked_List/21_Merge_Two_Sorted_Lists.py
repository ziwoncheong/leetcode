# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head=ListNode(-1)
        cursor=head
        
        while(l1 !=None and l2 != None):
            # l1이 더 클때
            if l1.val <= l2.val:
                cursor.next = l1
                l1 = l1.next
                
            # l2가 더 클때
            elif l1.val >l2.val:
                cursor.next = l2
                l2=l2.next
            cursor=cursor.next #Move cursor
            
        # 한 linked list가 끝에 도달했을 때
        # l1이 남았을 때
        if l1 != None:
            cursor.next = l1
        elif l2 != None:
            cursor.next = l2
        
        return head.next
