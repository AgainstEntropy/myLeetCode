# 合并 k 个有序链表
# Merge k Sorted Lists

from common import List, Optional, ListNode, create_linked_list, print_linked_list


class Solution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode(-float('inf'))

        for lst in lists:
            dummy_head = self.merge(dummy_head, lst)

        return dummy_head.next

    @staticmethod
    def merge(list1: Optional[ListNode], list2: Optional[ListNode]):
        dummy_head = ListNode(0)

        curr = dummy_head

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2

        return dummy_head.next


if __name__ == "__main__":
    test_cases = [
        # ([[1, 4, 5], [1, 3, 4], [2, 6]],),
        # ([],),
        # ([[]],),
        ([[],[-2],[-3,-2,1]],),
    ]

    for test_case in test_cases:
        lists = [create_linked_list(lst) for lst in test_case[0]]
        print_linked_list(Solution().merge_k_lists(lists))
