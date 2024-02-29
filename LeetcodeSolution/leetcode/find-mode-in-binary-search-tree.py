# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count={}
        result=[]
        if root and not root.right and not root.left:
            return [root.val]
        def helper(root):
            if not root:
                return []
            if root.val in count:
                count[root.val]+=1
            elif root.val not in count:
                count[root.val]=1
            helper(root.right)
            helper(root.left)
        helper(root)
        maxx=max(count.values())
        for key,value in count.items():
            if value==maxx:
                result.append(key)
        return result