# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        cur = head
        while cur:
            res.append(cur)
            cur=cur.next
        left = 0
        right = len(res)-1
        while left <= right:
            if res[left].val == res[right].val:
                left += 1
                right -= 1
            else:
                return False
        return True
            
        