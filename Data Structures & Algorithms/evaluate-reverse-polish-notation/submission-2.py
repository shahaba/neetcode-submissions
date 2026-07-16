class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '-', '*', '/'])

        def helper(x, y, op):
            if op == '+':
                return x + y
            elif op == '-':
                return x - y
            elif op == '*':
                return x * y
            else:
                return x / y

        for token in tokens:
            if token in ops:
                x = stack.pop()
                y = stack.pop()
                z = helper(y, x, token)
                
                stack.append(int(z))
                print(x, y, token, z, stack)
            else:
                stack.append(int(token))

        return stack.pop()