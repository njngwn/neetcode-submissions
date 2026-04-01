import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a/b)
        }

        stack = []

        for t in tokens:
            if t in ops:
                num1 = stack.pop()
                num2 = stack.pop()
                result = ops[t](num2, num1)
                stack.append(result)
            else:
                stack.append(int(t))

        return stack.pop()