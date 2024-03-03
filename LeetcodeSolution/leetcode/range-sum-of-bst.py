# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=0
        def dfs(root):
            nonlocal ans
            if not root:
                return ans
            curr=root.val
            if low<=curr<=high:
                ans+=curr
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ans
        