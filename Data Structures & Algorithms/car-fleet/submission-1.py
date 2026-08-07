class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0

        # 1. Sort positions and speeds descending
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, s in cars:
            
            stack.append((target - pos) / s)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        
        return len(stack)


    