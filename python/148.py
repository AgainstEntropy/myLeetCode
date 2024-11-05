# 排序链表
# Sort List

from common import ListNode, Optional, create_linked_list, print_linked_list


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        left, right = self.split(head)

        return self.merge(self.sortList(left), self.sortList(right))

    @staticmethod
    def split(head: Optional[ListNode]) -> tuple[Optional[ListNode]]:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        left = head

        return left, right

    @staticmethod
    def merge(left: Optional[ListNode], right: Optional[ListNode]):
        dummy_head = ListNode(0)

        curr = dummy_head

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        curr.next = left or right

        return dummy_head.next


if __name__ == "__main__":
    test_cases = [
        ([4, 2, 1, 3],),
        ([-1, 5, 3, 4, 0],),
    ]

    for test_case in test_cases:
        head = create_linked_list(test_case[0])
        print_linked_list(head)
        print_linked_list(Solution().sortList(head))
