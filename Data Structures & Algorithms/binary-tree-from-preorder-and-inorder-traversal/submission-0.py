# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        n = len(preorder)
        if not n:
            return None

        self.idx = 0

        def helper(inorder_chunk):
            if not inorder_chunk:
                return None

            root_node = preorder[self.idx]
            curr = TreeNode(root_node)
            self.idx += 1
            index = inorder_chunk.index(root_node)

            left_subtree = inorder_chunk[:index]
            right_subtree = inorder_chunk[index+1:]

            curr.left = helper(left_subtree)
            curr.right = helper(right_subtree)

            return curr

        return helper(inorder)