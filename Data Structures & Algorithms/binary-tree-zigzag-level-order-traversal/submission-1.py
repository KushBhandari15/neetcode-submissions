# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        res = []
        reverse = False
        queue = deque([root])

        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            
            if reverse:
                level = level[::-1]
            res.append(level)
            reverse = not reverse
        
        return res