# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        perivous=None
        while current:
            nxt=current.next
            current.next=perivous
            perivous=current
            current=nxt
        return perivous
                
        