class Solution:
    def partition(self, s: str) -> List[List[str]]:
    
        def is_pali(left, right):

            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True
        
        sol, res = [], []
        n = len(s)

        def helper(i):

            if i >= n:
                res.append(sol[:])
                return
            
            for j in range(i, n):
                if is_pali(i, j):
                    sol.append(s[i:j+1])
                    helper(j+1)
                    sol.pop()
                
        
        helper(0)
        return res
