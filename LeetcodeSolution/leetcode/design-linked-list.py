class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def get(self, index: int) -> int:
        if index>=self.size:
            return -1
        curr=self.head
        count=0
        while count!=index:
            curr=curr.next
            count+=1
        return curr.val
    def get_target(self, index: int) -> int:
        if index>=self.size:
            return -1
        curr=self.head
        count=0
        while count!=index:
            curr=curr.next
            count+=1
        return curr
    def addAtHead(self, val: int) -> None:
        node=Node(val)
        if not self.head:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head=node
        self.size+=1

        

    def addAtTail(self, val: int) -> None:
        node=Node(val)
        if not self.head:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        node=Node(val)
        if index>self.size:
            return
        if index==0:
            self.addAtHead(val)
            return
        if index==self.size:
            self.addAtTail(val)
            return
        prev=self.get_target(index-1)
        temp=prev.next
        prev.next=node
        node.next=temp
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.size:
            return 
        if index==0:
            temp=self.head
            self.head=temp.next
            self.size-=1
            if self.size==0:
                self.tail=None
            return
        if index==self.size-1:
            oldtail=self.tail
            newtail=self.get_target(index-1)
            self.tail=newtail
            newtail.next=None
            self.size-=1
            return
        prev=self.get_target(index-1)
        deleted_node=prev.next
        prev.next=deleted_node.next
        self.size-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)