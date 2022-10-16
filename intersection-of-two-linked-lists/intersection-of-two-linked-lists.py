# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, list1: ListNode, list2: ListNode) -> Optional[ListNode]:
        curA = list1
        curB = list2
        a, b = 0, 0
        while curA:
            a +=1
            curA = curA.next
        while curB:
            b += 1
            curB = curB.next
        if a>b:
            curL = list1
            curS = list2
            diff = a-b
        else:
            curL = list2
            curS = list1
            diff = b-a
        i=0
        while i<diff:
            i+=1
            curL = curL.next
            
        while curL != curS:
            curL = curL.next
            curS = curS.next
        return curL
        
        
        
		    
			    
		    
	    
        
        
        