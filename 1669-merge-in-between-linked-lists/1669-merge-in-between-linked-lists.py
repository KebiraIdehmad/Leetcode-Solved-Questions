# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        preva=list1
        for i in range(a-1):
            preva = preva.next #curr is in the position before a
            
        afterb = list1
        for i in range(b+1):
            afterb = afterb.next #the node after b
            
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        preva.next = list2
        tail2.next = afterb
        return list1
            
            
        
       