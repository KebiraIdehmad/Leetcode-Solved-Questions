# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#the linked list is sorted yeah
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        prev = head
        succ = head
        while prev and succ:
            if prev.val == succ.val:
                succ = succ.next
            else:
                prev.next = succ
                prev = succ
        if prev != succ:
            prev.next = None
        return head
            
                
        
       