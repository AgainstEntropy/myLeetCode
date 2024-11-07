# 最小栈
# Min Stack


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(val if not self.min_stack else min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    test_cases = [
        (
            ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[], [-2], [0], [-3], [], [], [], []],
        ),
    ]

    for method_calls, args in test_cases:
        min_stack = None
        for method_call, arg in zip(method_calls, args):
            if method_call == "MinStack":
                min_stack = MinStack()
            else:
                print(
                    f"call {method_call} with {arg}: {getattr(min_stack, method_call)(*arg)}"
                )
        print()
