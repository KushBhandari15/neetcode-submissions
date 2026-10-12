# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def get_path(node, target, path):
            if not node:
                return []

            if node == target:
                return path + [node]
            
            path1 = get_path(node.left, target, path + [node])
            path2 = get_path(node.right, target, path + [node])

            return path1 if path1 else path2
        
        first = set(reversed(get_path(root, p, [])))
        print(first)
        second = (get_path(root, q, []))

        for i in range(len(second) - 1, - 1, -1):
            if second[i] in first:
                print("here")
                return second[i]
        
        return root

        
