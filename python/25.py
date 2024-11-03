# K 个一组翻转链表
# Reverse Nodes in k-Group

from common import ListNode, Optional, create_linked_list, print_linked_list


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        max_reverse_time = n // k
        reverse_time = 0

        dummy_head = ListNode(next=head)

        left_tail = dummy_head

        while reverse_time < max_reverse_time:
            prev = left_tail
            curr = prev.next
            group_index = 1

            while group_index <= k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

                group_index += 1

            group_start = left_tail.next
            group_start.next = curr
            left_tail.next = prev

            left_tail = group_start

            reverse_time += 1

        return dummy_head.next

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3, 4, 5], 3),
    ]

    for head, k in test_cases:
        head = create_linked_list(head)
        print_linked_list(head)

        sol = Solution()
        res = sol.reverseKGroup(head, k)
        print_linked_list(res)
