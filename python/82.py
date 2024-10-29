# Remove Duplicates from Sorted List II
# 删除排序链表中的重复元素II

from common import ListNode, Optional, create_linked_list, print_linked_list


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head

        dummy_head = ListNode(next=head)

        slow = dummy_head
        fast = head
        fast_duplicated = False

        while fast.next:
            if fast.val == fast.next.val:
                fast_duplicated = True
            else:
                if not fast_duplicated:
                    slow.next = fast
                    slow = fast
                fast_duplicated = False

            fast = fast.next

        if slow:
            slow.next = None if fast_duplicated else fast

        return dummy_head.next


if __name__ == '__main__':
    test_cases = [
        ([],),
        ([None,],),
        ([1, 1, 2],),
        ([1,1,2,3,3],),
        ([1,1,1,2,3],),
        ([1,2,3,3,4,4,5],),
    ]

    sol = Solution()
    for case in test_cases:
        head = create_linked_list(case[0])
        print_linked_list(head)
        res = sol.deleteDuplicates(head)
        # print(case, '\n', res)
        print_linked_list(res)
        print()
