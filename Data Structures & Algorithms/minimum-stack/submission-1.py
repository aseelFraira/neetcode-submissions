class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        min_val = val
        if len(self.stack) > 0:
            min_val = min(val, self.stack[-1][1])
        self.stack.append([val,min_val])


    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
        

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][1]
        
