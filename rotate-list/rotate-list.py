# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        n, last = 1, head
        while last.next:
            last = last.next
            n += 1
        if k%n == 0:
            return head
        middle = head
        for i in range(n-k%n-1):
            middle = middle.next
        newhead = middle.next
        last.next=head
        middle.next = None
        return newhead
            
    