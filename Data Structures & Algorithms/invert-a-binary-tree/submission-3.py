# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
            
        queue = deque()
        queue.append(root)

        while queue:
            level = len(queue)
            for _ in range(level):
                curr = queue.popleft()
                left, right = None, None
                if curr.left:
                    left = curr.left
                    queue.append(curr.left)
                if curr.right:
                    right = curr.right
                    queue.append(curr.right)
                curr.left, curr.right = right, left

        return root
