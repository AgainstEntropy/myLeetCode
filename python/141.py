# 环形链表
# Linked List Cycle

from common import (
    ListNode,
    Optional,
    create_cycle_linked_list,
    create_linked_list,
    print_linked_list,
)


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False


if __name__ == "__main__":
    test_cases = [
        ([3, 2, 0, -4], 1),
        ([1, 2], 0),
        ([1], -1),
    ]

    for arr, pos in test_cases:
        head = create_linked_list(arr)
        print_linked_list(head)

        head_cycle = create_cycle_linked_list(arr, pos)
        print(Solution().hasCycle(head_cycle))
