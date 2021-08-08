"""
처음에 짠 코드
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min is None:
            self.min = val
        else:
            self.min = min(self.min, val)
        self.stack.append(val)

    def pop(self) -> None:
        poppedItem = self.stack.pop()
        if self.min == poppedItem:
            self.min = min(self.stack) if self.stack else None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min