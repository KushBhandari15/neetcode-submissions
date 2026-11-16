class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right; self.right.prev = self.left
        self.count = 0
        self.k = k
    
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            curr = Node(value)
            temp = self.right.prev
            temp.next = curr
            curr.prev = temp
            curr.next = self.right
            self.right.prev = curr
            self.count += 1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            temp = self.left.next.next
            self.left.next = temp
            temp.prev = self.left
            self.count -= 1
            return True
        return False

    def Front(self) -> int:
        return self.left.next.val if self.count > 0 else -1

    def Rear(self) -> int:
        return self.right.prev.val if self.count > 0 else -1

    def isEmpty(self) -> bool:
        return True if self.count == 0 else False

    def isFull(self) -> bool:
        return True if self.count >= self.k else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()