# 重排链表
# Reorder List

from common import ListNode, Optional, Tuple, create_linked_list, print_linked_list


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        left, right = self.split(head)
        self.merge(left, self.reverse(right))

    @staticmethod
    def split(
        head: Optional[ListNode],
    ) -> Tuple[Optional[ListNode], Optional[ListNode]]:
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        left = head
        right = slow.next
        slow.next = None

        return left, right

    @staticmethod
    def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    @staticmethod
    def merge(
        head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head = ListNode()
        curr = dummy_head
        curr1 = head1
        curr2 = head2
        while curr1 and curr2:
            curr.next = curr1
            curr1 = curr1.next
            curr = curr.next

            curr.next = curr2
            curr2 = curr2.next
            curr = curr.next

        curr.next = curr1 or curr2

        return dummy_head.next


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
    ]

    for arr in test_cases:
        head = create_linked_list(arr)
        print_linked_list(head)

        Solution().reorderList(head)
        print_linked_list(head)
