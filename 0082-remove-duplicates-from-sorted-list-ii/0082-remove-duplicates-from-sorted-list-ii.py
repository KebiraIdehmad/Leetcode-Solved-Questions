# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummyhead=dummy = ListNode(0,None)
        prev = head
        succ = head.next
        
        if prev.val != succ.val:
            dummy.next = prev
            dummy = dummy.next
            
            
        
        while succ:
            if succ.val == prev.val:
                succ = succ.next
            else:
                prev = succ
                succ = succ.next
                if succ and prev.val != succ.val:
                    dummy.next = prev
                    dummy = dummy.next
        if prev.next ==None and succ==None:
            dummy.next = prev
        else:
            dummy.next = None
        return dummyhead.next
            
        
        
        