class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        res = []

        for ast in asteroids:
            if ast > 0:
                res.append(ast)
            else:
                while res and res[-1] > 0 and abs(res[-1]) < abs(ast):
                    res.pop()
                if not res or res[-1] < 0:
                    res.append(ast)
                elif abs(res[-1]) == abs(ast):
                    res.pop()
            
        return res