# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, list1: ListNode, list2: ListNode) -> Optional[ListNode]:
        ptr1 = list1
        ptr2= list2
        l = set()
        while ptr1 != None:
            l.add(ptr1)
            ptr1 = ptr1.next
        while ptr2:
            if ptr2 in l:
                return ptr2
            l.add(ptr2)
            ptr2 = ptr2.next
        return None
        
	    
	    
	
	    
		    
		    
	    
		    
			    
		    
	    
        
        
        