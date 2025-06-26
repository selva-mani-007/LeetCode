"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n,r,c):
            all_same = True
            first_val = grid[r][c]

            for i in range(r,r+n):
                for j in range(c,c+n):
                    if grid[i][j] != first_val:
                        all_same = False
                        break
            if all_same:
                return Node(first_val,True)
            
            n = n//2

            topLeft = dfs(n,r,c)
            topRight = dfs(n,r,c+n)
            bottomLeft = dfs(n,r+n,c)
            bottomRight = dfs(n,r+n,c+n)

            return Node(0,False,topLeft,topRight,bottomLeft,bottomRight)
        return dfs(len(grid),0,0)
