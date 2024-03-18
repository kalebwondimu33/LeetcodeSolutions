# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root,curr_min,curr_max):
            nonlocal ans
            if not root:
                ans=max(ans,curr_max-curr_min)
                return
            curr_min=min(curr_min,root.val)
            curr_max=max(curr_max,root.val)
            dfs(root.left,curr_min,curr_max)
            dfs(root.right,curr_min,curr_max)
        ans=0
        dfs(root,root.val,root.val)
        return ans
        