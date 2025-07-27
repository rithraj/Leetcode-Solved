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
        # Create a hashmap to hold the original
        if not head:
            return None
            
        nodes = {}
        node = head

        while node:
            nodes[node] = Node(node.val)
            node = node.next
        
        node = head
        while node:
            nodes[node].next = nodes.get(node.next)
            nodes[node].random = nodes.get(node.random)
            node = node.next
        
        return nodes[head]
        
        
        