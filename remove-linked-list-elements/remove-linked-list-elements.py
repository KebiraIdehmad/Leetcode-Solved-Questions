# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        dummy = ListNode(0,head)
        
        while head:
            if head.val == val:
                head = head.next
            else: break
        
        while cur:
            if cur.val == val:
                cur = cur.next
                dummy.next = cur
                
                
            else:
                dummy = cur
                cur = cur.next
        return head
            
    
                
        
     

            
        
                
       