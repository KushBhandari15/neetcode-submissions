# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def find_path(node, curr_path, final):
            
            if not node:
                return False, None
                
            curr_path.append(node)
            if node == final:
                return True, curr_path
            
            found, path = find_path(node.left, curr_path, final)
            if found:
                return True, path

            found, path = find_path(node.right, curr_path, final)
            if found:
                return True, path
            
            curr_path.pop()
            return False, []
        
        _, path1 = find_path(root, [], p)
        _, path2 = find_path(root, [], q)  

        n, m = len(path1), len(path2)
        i, j = 0, 0
        res = TreeNode()
        while i < n and j < m:
            if path1[i] == path2[j]:
                res = path1[i]
                i += 1
                j += 1
            else:
                return res
        return res