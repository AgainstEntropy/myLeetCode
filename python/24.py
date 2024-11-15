# 两两交换链表中的节点
# Swap Nodes in Pairs

from common import ListNode, Optional, create_linked_list, print_linked_list


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head

        prev = dummy_head
        curr = head
        while curr and curr.next:
            next = curr.next
            nnext = next.next
            next.next = curr
            prev.next = next
            curr.next = nnext

            prev = curr
            curr = nnext

        return dummy_head.next


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4],
        [],
        [1],
        [1, 2, 3],
    ]

    sol = Solution()

    for nums in test_cases:
        head = create_linked_list(nums)
        print_linked_list(head)
        print_linked_list(sol.swapPairs(head))
