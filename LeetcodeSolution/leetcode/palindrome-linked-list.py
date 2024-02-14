# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        num=[]
        while head:
            num.append(head.val)
            head=head.next
        l,r=0,len(num)-1
        while l<=r:
            if num[l]!=num[r]:
                return False
            l+=1
            r-=1
        return True
        