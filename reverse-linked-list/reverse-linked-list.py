# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        temp2 = None
        while head != None :
            temp2 = head.next
            head.next = temp
            temp = head
            head = temp2
        return temp
          
            