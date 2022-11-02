# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        counter=0
        while curr:
            counter += 1
            curr = curr.next
        #find k node from the beginning
        start = head
        for i in range(k-1):
            start = start.next
        startval=start.val
        #find k node from the end
        end = head
        for i in range(counter-k):
            end = end.next
        start.val, end.val = end.val, start.val
        
        return head
            
        
            
        