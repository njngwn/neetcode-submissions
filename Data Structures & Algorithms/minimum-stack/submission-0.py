class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_value = min(self.getMin(), val) if self.stack else val
        self.stack.append((val, min_value))
        
    def pop(self) -> None:
        if self.stack:
            del self.stack[-1]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return -1

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return -1
        
