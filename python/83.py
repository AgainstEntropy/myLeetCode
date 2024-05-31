# Remove Duplicates from Sorted List
# 删除排序链表中的重复元素

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = set()

        prev = None
        curr = head
        while curr:
            if curr.val not in values:
                values.add(curr.val)
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next

        return head

    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast:
            if slow.val != fast.val:
                slow.next = fast
                slow = fast
            fast = fast.next

        if slow:
            slow.next = None

        return head


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
        ([None,],),
        ([1, 1, 2],),
        ([1,1,2,3,3],)
    ]

    sol = Solution()
    for case in test_cases:
        head = create_linked_list(case[0])
        print_linked_list(head)
        # res = sol.deleteDuplicates(head)
        res = sol.deleteDuplicates2(head)
        # print(case, '\n', res)
        print_linked_list(res)