from typing import List, Optional  # noqa: F401


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: "ListNode" = None):
        self.val = val
        self.next = next

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


def create_cycle_linked_list(arr, pos) -> Optional[ListNode]:

    head = create_linked_list(arr)
    if pos == -1:
        return head

    curr = head
    for _ in range(pos):
        curr = curr.next
    cycle_node = curr

    while curr.next:
        curr = curr.next
    curr.next = cycle_node

    return head
