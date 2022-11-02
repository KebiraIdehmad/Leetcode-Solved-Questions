# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead  = ListNode(0,None)
        dummy = dummyhead
        
        fast = head.next
        counter = 0
        while fast.next : #this may cause somethig
            
            while fast.next.val !=0:
                counter += fast.val
                fast = fast.next
            fast.val += counter
            dummy.next = fast
            dummy = dummy.next
            
            
            fast = fast.next
            if fast.next == None:
                dummy.next = None
            
                
            counter = 0
        return dummyhead.next
                
        
        
        