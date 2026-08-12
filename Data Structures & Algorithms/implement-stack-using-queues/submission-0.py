class MyStack:

    def __init__(self):
        self.front = deque()
        self.hold = deque()

    def push(self, x: int) -> None:
        while self.front:
            self.hold.append(self.front.popleft())
        self.front.append(x)
        while self.hold:
            self.front.append(self.hold.popleft())

    def pop(self) -> int:
        return self.front.popleft()

    def top(self) -> int:
        return self.front[0]

    def empty(self) -> bool:
        return not self.front


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()