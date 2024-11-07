# 用栈实现队列
# Implement Queue using Stacks


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

        self.in_stack1 = True

    def push(self, x: int) -> None:
        if not self.in_stack1:
            self.to_stack1()
        self.stack1.append(x)

    def pop(self) -> int:
        if self.in_stack1:
            self.to_stack2()

        return self.stack2.pop()

    def peek(self) -> int:
        if self.in_stack1:
            self.to_stack2()

        return self.stack2[-1]

    def empty(self) -> bool:
        if self.in_stack1:
            return len(self.stack1) == 0
        else:
            return len(self.stack2) == 0

    def to_stack1(self) -> None:
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.in_stack1 = True

    def to_stack2(self) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.in_stack1 = False


if __name__ == "__main__":
    test_cases = [
        (
            ["MyQueue", "push", "push", "peek", "pop", "empty"],
            [[], [1], [2], [], [], []],
        ),
    ]

    for method_calls, args in test_cases:
        my_queue = None
        for method_call, arg in zip(method_calls, args):
            if method_call == "MyQueue":
                my_queue = MyQueue()
            else:
                print(
                    f"call {method_call} with {arg}: {getattr(my_queue, method_call)(*arg)}"
                )
        print()
