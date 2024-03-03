# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        countA=0
        countB=0
        curr=headA
        while curr:
            countA+=1
            curr=curr.next
        cu=headB
        while cu:
            countB+=1
            cu=cu.next
        diff=abs(countA-countB)
        
        left=None
        if countB>countA:
            left=headB
            for i in range(diff):
                left=left.next
            right=headA
            while left and right:
                if left==right:
                    return left
                left=left.next
                right=right.next
            return None
        else:
            left=headA
            for i in range(diff):
                left=left.next
            right=headB
            while left and right:
                if left==right:
                    return left
                left=left.next
                right=right.next
            return None
        




        return None
        

        