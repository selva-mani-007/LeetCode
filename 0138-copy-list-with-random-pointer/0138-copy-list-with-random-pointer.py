"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        current = head
        copied_head = head.next
        while current:
            copied_node = current.next
            current.next = copied_node.next
            copied_node.next = copied_node.next.next if copied_node.next else None
            current = current.next
        return copied_head

        


'''
        current = head
        node_map = {}

        while current:
            node_map[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            node_map[current].next = node_map.get(current.next)
            node_map[current].random = node_map.get(current.random)
            current = current.next

        return node_map[head]
'''