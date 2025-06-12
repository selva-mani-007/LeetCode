# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root,maxval):
            if not root:
                return 0

            isGood = 1 if root.val >= maxval else 0
            maxval = max(maxval,root.val)

            left = dfs(root.right,maxval)
            right = dfs(root.left,maxval)  #left,right swapped for nothing

            return isGood + left + right

        return dfs(root,root.val)