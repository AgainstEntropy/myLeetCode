# LRU 缓存
# LRU Cache


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        from collections import OrderedDict

        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        val = self.cache.pop(key)
        return self.cache.setdefault(key, val)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)


if __name__ == "__main__":
    test_cases = [
        (
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
        )
    ]

    for method_calls, args in test_cases:
        lru_cache = None
        for method_call, arg in zip(method_calls, args):
            if method_call == "LRUCache":
                lru_cache = LRUCache(arg[0])
            else:
                print(
                    f"call {method_call} with {arg}: {getattr(lru_cache, method_call)(*arg)}"
                )
        print()
