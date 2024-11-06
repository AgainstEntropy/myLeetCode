# 删除链表的倒数第 N 个节点
# Remove Nth Node From End of List

from common import ListNode, Optional, create_linked_list, print_linked_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head

        dummy_head = ListNode(next=head)

        slow = fast = dummy_head
        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy_head.next


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2),
        ([1, 2], 1),
        ([1, 2], 2),
        ([1], 1),
    ]

    for arr, n in test_cases:
        head = create_linked_list(arr)
        print_linked_list(head)

        head = Solution().removeNthFromEnd(head, n)
        print_linked_list(head)
