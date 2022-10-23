# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        counter = 0
        while cur:
            counter += 1
            cur = cur.next
        cur = head
        number = 0
        counter -= 1
        while cur:
            number += cur.val*2**counter
            counter -= 1
            cur = cur.next
        return number
            
            
            
        