class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operation = "+-/*"
        for token in tokens:
            if token in operation:
                first = stack.pop()
                second = stack.pop()
                if token == "+":
                    stack.append(first+second)
                elif token == "-":
                    stack.append(second-first)
                elif token == "*":
                    stack.append(first*second)
                elif token == "/":
                    stack.append(int(second/first))
            else:
                stack.append(int(token))
        
        print(stack)
        return stack[0]


