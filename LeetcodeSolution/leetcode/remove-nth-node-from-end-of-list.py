# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(None)
        dummy.next=head
        
        temp=dummy
        prevNode=dummy

        length=0
        while temp:
            length+=1
            temp=temp.next
            
        deletedNode=length-n

        for i in range(deletedNode-1):
            prevNode=prevNode.next

        deletedNode=prevNode.next
        prevNode.next=deletedNode.next
        deletedNode.next=None
        return dummy.next

        