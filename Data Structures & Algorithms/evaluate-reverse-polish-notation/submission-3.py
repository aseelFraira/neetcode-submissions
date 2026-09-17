class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+','-','/','*'}
        stack = []
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            elif stack:
                rhs = stack.pop()
                lhs = stack.pop()
                if token == "+":
                    result = lhs + rhs
                elif token == "-":
                    result = lhs - rhs
                elif token == "*":
                    result = lhs * rhs
                else:
                    result = int(lhs / rhs)
                stack.append(result)

        return stack[0]
        