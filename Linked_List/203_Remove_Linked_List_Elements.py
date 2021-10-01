# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if head ==None:
            return None
        
        node1 = node2 = head
        node2 = node1.next
        while(node2!=None):
            if node2.val == val:
                node1.next = node2.next
                node2 = node2.next
            else:
                node2 = node2.next
                node1 = node1.next
               
            
        if(head.val == val):
            return head.next
        else: return head
        
        
        
 class Solution2:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
            while head and head.val == val: 
                head = head.next 
                
            if not head: 
                return head 
            
            next_node = head 
            while next_node and next_node.next:
                if next_node.next.val == val: 
                    next_node.next = next_node.next.next 
                else: 
                    next_node = next_node.next 
                    
            return head
