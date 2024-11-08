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
        if node is None:
            return None

        visited = {}

        new_node = Node(node.val)

        queue = collections.deque()
        queue.append(node)
        visited[node] = new_node
        while queue:
            curr = queue.popleft()
            # print(f"Curr val: {curr.val}")
            for neighbor in curr.neighbors:
                # print(neighbor.val)
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = Node(neighbor.val)

                visited[curr].neighbors.append(visited[neighbor])
        return new_node