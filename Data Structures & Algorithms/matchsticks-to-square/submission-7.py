class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        n = len(matchsticks)

        if n < 4:
            return False
        
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        side_length = total // 4

        sides = [0, 0, 0, 0]
        matchsticks.sort(reverse=True)

        def dfs(idx):
            if idx >= n:
                return all(side == side_length for side in sides)

            for i in range(4):
                if sides[i] + matchsticks[idx] <= side_length:
                    sides[i] += matchsticks[idx]
                    if dfs(idx + 1):
                        return True
                    sides[i] -= matchsticks[idx]
                    if sides[i] == 0:
                        break
            
            return False
        
        return dfs(0)