# DOUBLY LINKED LIST SOLUTION:
class ListNode:
    def __init__(self, val=0, nextNode=None, prevNode=None):
        self.val=val
        self.next=nextNode
        self.prev=prevNode
class MyLinkedList:
    def __init__(self):
        self.size=0
        self.head=ListNode()
        self.tail=ListNode()
        self.head.next=self.tail
        self.tail.prev=self.head
    def get(self, index):
        if index>=self.size:
            return -1
        if index <= self.size//2:
            cur = self.head
            for i in range(index+1):
                cur = cur.next
        else:
            cur = self.tail
            for i in range(self.size-index):
                cur = cur.prev
        return cur.val
    
    def addAtHead(self, val):
        self.addAtIndex(0, val)
        
    def addAtTail(self, val):
        self.addAtIndex(self.size, val)
    def addAtIndex(self, index, val):
        if index>self.size:
            return 
        if index<=self.size//2:
            pred=self.head
            for i in range(index):
                pred=pred.next
            succ=pred.next
        
        else:
            succ = self.tail
            for i in range(self.size-index):
                succ = succ.prev
            pred = succ.prev
        new_node=ListNode(val)    
        new_node.next=succ
        new_node.prev=pred
        pred.next=new_node
        succ.prev=new_node
        self.size += 1
    
    def deleteAtIndex(self, index):
        if index>=self.size:
            return -1
        if index<=self.size//2:
            pred = self.head
            for i in range(index):
                pred = pred.next
            succ=pred.next.next
        else:
            succ=self.tail
            for i in range(self.size-index-1):
                succ = succ.prev
            pred = succ.prev.prev
        pred.next=succ
        succ.prev=pred
        self.size -= 1
        
        
            
    
            
       
    
        
        
        
        
        
            
            
    