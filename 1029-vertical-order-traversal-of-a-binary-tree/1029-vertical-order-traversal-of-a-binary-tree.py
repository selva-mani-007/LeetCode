# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []

        def dfs(node,row,col):
            if not node:
                return
            
            nodes.append((col,row,node.val))
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)
        
        dfs(root,0,0)
        nodes.sort()

        result = []
        cur_col = float('-inf')

        for col,row,val in nodes:
            if col != cur_col:
                cur_col = col
                result.append([])
            result[-1].append(val)
        
        return result