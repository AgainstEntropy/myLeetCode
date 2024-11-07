# 两数相加
# Add Two Numbers

from common import ListNode, Optional, create_linked_list, print_linked_list


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy_head = ListNode()

        curr = dummy_head
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            sum %= 10

            curr.next = ListNode(val=sum)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        rest = l1 or l2
        while rest:
            sum = rest.val + carry
            carry = sum // 10
            sum %= 10

            curr.next = ListNode(val=sum)
            curr = curr.next
            rest = rest.next

        if carry != 0:
            curr.next = ListNode(val=carry)

        return dummy_head.next


if __name__ == "__main__":
    test_cases = [
        ([2, 4, 3], [5, 6, 4]),
        ([0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]),
    ]

    for l1, l2 in test_cases:
        l1_head = create_linked_list(l1)
        print_linked_list(l1_head)
        l2_head = create_linked_list(l2)
        print_linked_list(l2_head)

        print_linked_list(Solution().addTwoNumbers(l1_head, l2_head))
