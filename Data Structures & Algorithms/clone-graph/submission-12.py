"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, node):
        if node in self.oldToNew:
            return self.oldToNew[node]
        copy_node = Node(node.val)
        self.oldToNew[node] = copy_node
        for neighbor in node.neighbors:
            copy_node.neighbors.append(self.dfs(neighbor))
        return copy_node
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.oldToNew = {}
        return self.dfs(node) if node else None
        