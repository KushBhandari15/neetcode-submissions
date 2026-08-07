class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < temperature:
                last = stack.pop()
                res[last] = i - last
            
            stack.append(i)
        
        return res