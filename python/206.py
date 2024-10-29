# Reverse Linked List
# 反转链表

from common import ListNode, Optional, create_linked_list, print_linked_list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2],
        [1],
        [],
    ]

    sol = Solution()
    for case in test_cases:
        head = create_linked_list(case)
        print_linked_list(head)
        res = sol.reverseList(head)
        print_linked_list(res)
        print()
