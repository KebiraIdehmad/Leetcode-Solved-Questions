# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a = 0
        cur = head 
        prev = None
        while cur:
            a+=1
            cur = cur.next
        diff = a-n+1
        idx =0
        cur = head
        while idx != diff:
            idx += 1
            if idx == diff and prev==None:
                return head.next
            elif idx == diff:
                prev.next = cur.next
                break
            prev = cur
            cur = cur.next
        return head

        
      