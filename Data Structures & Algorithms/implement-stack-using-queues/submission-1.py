import queue

class MyStack:

    def __init__(self):
        self.queues = [queue.Queue(), queue.Queue()]

    def push(self, x: int) -> None:
        self.queues[0].put(x)

    def pop(self) -> int:
        while not self.queues[0].empty():
            temp = self.queues[0].get()
            if not self.queues[0].empty():
                self.queues[1].put(temp)
        self.switch_queues()
        return temp

    def top(self) -> int:
        while not self.queues[0].empty():
            temp = self.queues[0].get()
            self.queues[1].put(temp)
        self.switch_queues()
        return temp

    def empty(self) -> bool:
        return self.queues[0].empty()

    def switch_queues(self):
        self.queues[1], self.queues[0] = self.queues[0], self.queues[1]
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()