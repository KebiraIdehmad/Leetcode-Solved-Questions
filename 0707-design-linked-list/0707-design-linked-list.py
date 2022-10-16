class node :
    def __init__(self,data=None):
        self.data=data
        self.next=None
class MyLinkedList:
    
    def __init__(self):
        self.head=node()
    def length(self): 
        cur = self.head
        total=0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    def get(self, index: int) -> int:
        idx=0
        cur = self.head
        if index>=self.length():
            return -1
        while True :
            cur = cur.next
            if idx==index:
                return cur.data
            idx+=1
                
    def addAtHead(self, val: int) -> None:
        new_node=node(val)
        cur = self.head
        new_node.next=cur.next
        cur.next=new_node

    def addAtTail(self, val: int) -> None:
        new_node=node(val)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.length():
            return
        cur=self.head
        new_node=node(val)
        idx=0
        while True:
            if idx==index:
                new_node.next=cur.next
                cur.next=new_node
                return
            cur = cur.next
            idx+=1
                         
    def deleteAtIndex(self, index: int) -> None:
        if index>=self.length():
            return
        idx=0
        cur = self.head
        while True :
            last_node = cur
            cur = cur.next
            if idx==index:
                last_node.next=cur.next
                return
            idx+=1
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)