# 回文链表
# Palindrome Linked List

from common import ListNode, Optional, create_linked_list, print_linked_list


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        half_index = n // 2

        dummy_head = ListNode(next=head)

        # reverse the first half
        prev = dummy_head
        curr = prev.next

        index = 1
        while curr and index <= half_index:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            index += 1

        head.next = curr
        dummy_head.next = prev

        # compare the first half and the second half
        curr1 = prev
        curr2 = curr if n % 2 == 0 else curr.next
        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.next
            curr2 = curr2.next

        return True


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 1],),
        ([1, 2, 3, 2, 1],),
        ([1, 2],),
        ([1],),
        ([],),
    ]

    for test_case in test_cases:
        head = create_linked_list(test_case[0])
        print_linked_list(head)
        print(Solution().isPalindrome(head))
