# 反转链表 II
# Reverse Linked List II

from common import ListNode, Optional, create_linked_list, print_linked_list


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy_head = ListNode(next=head)
        index = 1

        left_tail = dummy_head

        while left_tail.next and index < left:
            left_tail = left_tail.next
            index += 1

        prev = left_tail
        curr = prev.next

        while curr and index <= right:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            index += 1

        left_tail.next.next = curr
        left_tail.next = prev

        return dummy_head.next


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2, 4),
        ([5], 1, 1),
    ]

    sol = Solution()
    for case in test_cases:
        head = create_linked_list(case[0])
        print_linked_list(head)
        case = (head, *case[1:])

        res = sol.reverseBetween(*case)

        print_linked_list(res)
        print()
