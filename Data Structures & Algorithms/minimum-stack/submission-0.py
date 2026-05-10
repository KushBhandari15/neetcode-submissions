class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        self.stack.append(self.min)
        self.stack.append(val)
        return None

    def pop(self) -> None:
        self.stack.pop()
        self.stack.pop()
        self.min = self.getMin()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) > 1:
            return self.stack[-2]
        return float('inf')
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()