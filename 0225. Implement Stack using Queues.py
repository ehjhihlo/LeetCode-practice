class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue2.insert(0, x)
        while self.queue1:
            self.queue2.insert(0, self.queue1.pop())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.pop()

    def top(self) -> int:
        return self.queue1[-1]

    def empty(self) -> bool:
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
