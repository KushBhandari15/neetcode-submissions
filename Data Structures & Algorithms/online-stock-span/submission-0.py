class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        
        self.stack.append(price)
        curr = self.stack.copy()

        res = 0
        while curr and curr[-1] <= price:
            res += 1
            curr.pop()
        
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)