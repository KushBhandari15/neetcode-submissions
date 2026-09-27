class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def childrens(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            
            return res

        if "0000" in deadends:
            return -1 

        queue = deque()
        visited = set(deadends)
        queue.append(["0000", 0]) # curr_lock, operation took to come here
    
        while queue:
            lock, op = queue.popleft()
            if lock == target:
                return op
            
            for child in childrens(lock):
                if child not in visited:
                    visited.add(child)
                    queue.append([child, op + 1])
            
        return -1
