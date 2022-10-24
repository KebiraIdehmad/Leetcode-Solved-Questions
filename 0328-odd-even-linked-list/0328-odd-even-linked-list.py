# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None or head.next == None or not head.next.next:
            return head
        oddptr = current = head 
        evenptr = head_evenptr= head.next
        i = 1
        while current:
            if i>2 and i%2  != 0:
                oddptr.next = current
                oddptr = current
            elif i>2 and i%2 ==0:
                evenptr.next = current
                evenptr = current
            current = current.next
            i += 1
        evenptr.next = None
        oddptr.next = head_evenptr
        return head