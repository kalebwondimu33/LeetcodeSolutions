# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        result=[]
        current=head
        while current:
            result.append(current.val)
            current=current.next
        output=[0]*len(result)
        stack=[]
        for index,value in enumerate(result):
            while stack and result[stack[-1]]<value:
                output[stack.pop()]=value
            stack.append(index)
        return output
            
        