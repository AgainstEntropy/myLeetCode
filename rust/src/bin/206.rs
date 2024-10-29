// Reverse Linked List
// 反转链表

use leetcode::common::{ListNode, create_linked_list, print_linked_list};

struct Solution {}

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev = None;
        let mut curr = head;
        let mut next;

        while let Some(mut node) = curr {
            next = node.next;
            node.next = prev;
            prev = Some(node);
            curr = next;
        }
        prev
    }
}

fn main() {
    let cases = vec![
        vec![1, 2, 3, 4, 5],
        vec![1, 2],
        vec![],
    ];

    for case in cases {
        let head = create_linked_list(case);
        print_linked_list(head.clone());
        let new_head: Option<Box<ListNode>> = Solution::reverse_list(head);
        print_linked_list(new_head);
        println!();
    }
}