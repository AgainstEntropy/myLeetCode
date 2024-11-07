# 用队列实现栈
# Implement Stack using Queues


class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

        return self.queue.pop(0)

    def top(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

        res = self.queue[0]

        self.queue.append(self.queue.pop(0))

        return res

    def empty(self) -> bool:
        return len(self.queue) == 0


if __name__ == "__main__":
    test_cases = [
        (
            ["MyStack", "push", "push", "top", "pop", "empty"],
            [[], [1], [2], [], [], []],
        ),
    ]

    for method_calls, args in test_cases:
        my_stack = None
        for method_call, arg in zip(method_calls, args):
            if method_call == "MyStack":
                my_stack = MyStack()
            else:
                print(getattr(my_stack, method_call)(*arg))
        print()
