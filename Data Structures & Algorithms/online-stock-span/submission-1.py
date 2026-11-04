class StockSpanner:

    def __init__(self):
        self.stack = []
        self.span = []

    def next(self, price: int) -> int:

        self.stack.append(price)
        n = len(self.stack)

        curr_span = 1
        idx = n - 2
        while idx >= 0 and self.stack[idx] <= price:
            curr_span += self.span[idx] 
            idx -= self.span[idx]
        
        self.span.append(curr_span)

        return curr_span