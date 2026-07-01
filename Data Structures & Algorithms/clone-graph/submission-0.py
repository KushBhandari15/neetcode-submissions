"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
import copy
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        cloned_map = {}
        seen = set()
        stack = [node]

        res = Node(node.val)
        cloned_map[node] = res
        stack2 = [res]

        seen.add(node)
        
        while stack:
            curr = stack.pop()
            curr_copy = stack2.pop()

            for neighbor in curr.neighbors:
                if neighbor not in seen:
                    stack.append(neighbor)
                    seen.add(neighbor)

                    newNode = Node(neighbor.val)
                    cloned_map[neighbor] = newNode

                    curr_copy.neighbors.append(newNode)
                    stack2.append(newNode)
                else:
                    existing_clone = cloned_map[neighbor]
                    curr_copy.neighbors.append(existing_clone)

        return res


                