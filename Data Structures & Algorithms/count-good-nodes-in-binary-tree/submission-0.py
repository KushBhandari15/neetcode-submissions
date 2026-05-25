# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(node, current_max):
            if not node:
                return 0

            res = 0
            if node.val >= current_max:
                print("Good node: ", node.val)
                res += 1
            if node.left:
                res += helper(node.left, max(current_max, node.val))
            if node.right:
                res += helper(node.right, max(current_max, node.val))

            return res
        
        return helper(root, -101)
                