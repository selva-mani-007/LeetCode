"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        visited = set()
        start = node
        stk = [start]
        visited.add(start)
        o_to_n = {}

        while stk:
            curr = stk.pop()
            o_to_n[curr] = Node(curr.val)

            for nei in curr.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stk.append(nei)
        
        for old_node,new_node in o_to_n.items():
            for nei in old_node.neighbors:
                new_nei = o_to_n[nei]
                new_node.neighbors.append(new_nei)

        return o_to_n[start]
