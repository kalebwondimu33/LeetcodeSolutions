# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return None
        hare=head
        tortoise=head
        while hare and hare.next:
            hare=hare.next.next
            tortoise=tortoise.next
            if hare==tortoise:
                break
        if tortoise!=hare:
            return None
        pointer=head
        while pointer!=tortoise:
            pointer=pointer.next
            tortoise=tortoise.next
        return tortoise
        