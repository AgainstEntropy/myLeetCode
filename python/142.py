# 环形链表 II
# Linked List Cycle II

from common import (
    ListNode,
    Optional,
    create_cycle_linked_list,
    create_linked_list,
    print_linked_list,
)


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if fast != slow:
            return None

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


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
        enter_node = Solution().detectCycle(head_cycle)
        print(enter_node and enter_node.val)
