# 相交链表
# Intersection of Two Linked Lists

from common import (
    ListNode,
    Optional,
    create_intersection_linked_list,
    print_linked_list,
)


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:

        currA = headA
        currB = headB

        while currA != currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA

        return currA


if __name__ == "__main__":
    test_cases = [
        ([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2),
        ([1, 9, 1, 2, 4], [3, 2, 4], 3),
        ([2, 6, 4], [1, 5], -1),
    ]

    for arr1, arr2, pos1 in test_cases:
        head1, head2 = create_intersection_linked_list(arr1, arr2, pos1)
        print_linked_list(head1)
        print_linked_list(head2)

        intersection_node = Solution().getIntersectionNode(head1, head2)
        print(intersection_node and intersection_node.val)
