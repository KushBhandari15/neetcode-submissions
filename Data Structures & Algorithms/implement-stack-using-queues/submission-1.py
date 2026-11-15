class MyStack:

    def __init__(self):
        self.queue = deque()
        self.helper = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        curr = self.queue.popleft()
        while self.queue:
            self.helper.append(curr)
            curr = self.queue.popleft()
        
        while self.helper:
            tmp = self.helper.popleft()
            self.queue.append(tmp)
        
        return curr


    def top(self) -> int:
        curr = -1
        while self.queue:
            curr = self.queue.popleft()
            self.helper.append(curr)
        
        while self.helper:
            tmp = self.helper.popleft()
            self.queue.append(tmp)
        
        return curr

    def empty(self) -> bool:
        return False if self.queue else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()