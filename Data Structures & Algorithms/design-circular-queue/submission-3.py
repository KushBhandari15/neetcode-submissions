class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue1 = []

    def enQueue(self, value: int) -> bool:
        if len(self.queue1) >= self.k:
            return False
        self.queue1.append(value)
        return True

    def deQueue(self) -> bool:
        n = len(self.queue1)
        if not n:
            return False
        self.queue1.pop(0)
        return True

    def Front(self) -> int:
        print(self.queue1)
        return self.queue1[0] if len(self.queue1) > 0 else -1

    def Rear(self) -> int:
        print(self.queue1)
        return self.queue1[-1] if len(self.queue1) > 0 else -1

    def isEmpty(self) -> bool:
        return len(self.queue1) <= 0

    def isFull(self) -> bool:
        return len(self.queue1) >= self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()