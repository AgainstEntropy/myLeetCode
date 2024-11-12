from typing import List, Optional, Tuple  # noqa: F401


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: "ListNode" = None):
        self.val = val
        self.next = next


def create_linked_list(
    arr: List, return_tail=False
) -> Optional[ListNode] | Tuple[Optional[ListNode], Optional[ListNode]]:
    if not arr:
        return None

    head = ListNode(arr[0])
    node = head
    for i in arr[1:]:
        node.next = ListNode(i)
        node = node.next

    if return_tail:
        return head, node

    return head


def print_linked_list(head: Optional[ListNode]):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('None')


def create_cycle_linked_list(arr: List, pos: int) -> Optional[ListNode]:
    head, tail = create_linked_list(arr, return_tail=True)
    if pos == -1:
        return head

    curr = head
    for _ in range(pos):
        curr = curr.next
    cycle_node = curr

    tail.next = cycle_node

    return head


def create_intersection_linked_list(
    arr1: List, arr2: List, pos1: int
) -> Optional[ListNode]:
    if pos1 == -1:
        head1 = create_linked_list(arr1)
        head2 = create_linked_list(arr2)
        return head1, head2

    head1, tail1 = create_linked_list(arr1[:pos1], return_tail=True)
    pos2 = len(arr2) - len(arr1) + pos1
    head2, tail2 = create_linked_list(arr2[:pos2], return_tail=True)

    head_common = create_linked_list(arr1[pos1:])

    tail1.next = head_common
    tail2.next = head_common

    return head1, head2


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(arr: List[int]) -> Optional[TreeNode]:
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        node = queue.pop(0)
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)
