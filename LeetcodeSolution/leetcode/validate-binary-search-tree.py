# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root,left,right):
            if not root:
                return True
            if not (root.val>left and root.val<right):
                return False
            return (valid(root.left,left,root.val) and valid(root.right,root.val,right))
        return valid(root,float("-inf"),float("inf"))