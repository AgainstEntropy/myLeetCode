# LCR 140. 训练计划 II
# 链表中倒数第k个节点

from common import Optional, ListNode, create_linked_list, print_linked_list


class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        slow = fast = head
        for _ in range(cnt):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow


if __name__ == "__main__":
    test_cases = [
        ([2, 4, 7, 8], 1),
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3, 4, 5], 5),
    ]

    sol = Solution()

    for arr, cnt in test_cases:
        linked_list = create_linked_list(arr)
        print_linked_list(linked_list)
        print(sol.trainingPlan(linked_list, cnt).val)
