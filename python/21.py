# 合并两个有序链表
# Merge Two Sorted Lists

from common import ListNode, Optional, create_linked_list, print_linked_list


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy_head = ListNode()
        curr = dummy_head

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        curr.next = list1 if list1 else list2

        return dummy_head.next


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4], [1, 3, 4]),
        ([1, 2, 4], [])
    ]

    for test_case in test_cases:
        head1 = create_linked_list(test_case[0])
        head2 = create_linked_list(test_case[1])
        print_linked_list(head1)
        print_linked_list(head2)
        print_linked_list(Solution().mergeTwoLists(head1, head2))
