# Reverse Linked List
# 反转链表

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


def create_linked_list(arr) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    node = head
    for i in arr[1:]:
        node.next = ListNode(i)
        node = node.next
    return head


def print_linked_list(head: Optional[ListNode]):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('None')


if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2],
        [1],
        [],
    ]

    sol = Solution()
    for case in test_cases:
        head = create_linked_list(case)
        print_linked_list(head)
        res = sol.reverseList(head)
        print_linked_list(res)
        print()
