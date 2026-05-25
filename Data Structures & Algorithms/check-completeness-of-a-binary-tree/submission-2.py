class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([root])
        seen_null = False
        
        while queue:
            n = len(queue)
            for i in range(n):
                curr = queue.popleft()
                if curr.left:
                    if seen_null:
                        return False
                    queue.append(curr.left)
                else:
                    seen_null = True
                
                if curr.right:
                    if seen_null:
                        return False
                    queue.append(curr.right)
                else:
                    seen_null = True
            
        return True