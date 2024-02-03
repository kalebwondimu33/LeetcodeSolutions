# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=node=head
        len_list=0
        while current:
            len_list+=1
            current=current.next
        middle=len_list//2
        count=0
        while node:
            if count==middle:
                return node
            else:
                count+=1
                node=node.next
        
        
        
        
        