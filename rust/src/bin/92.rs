// 反转链表 II
// Reverse Linked List II

use leetcode::common::{ListNode, create_linked_list, print_linked_list};

struct Solution {}

impl Solution {
    pub fn reverse_between(head: Option<Box<ListNode>>, left: i32, right: i32) -> Option<Box<ListNode>> {
        if head.is_none() || head.as_ref().unwrap().next.is_none() {
            return head;
        }

        let mut dummy_head = Some(Box::new(ListNode::new(0)));
        dummy_head.as_mut().unwrap().next = head;
        let mut left_tail = &mut dummy_head;

        // Move `left_tail` to the node just before the `left` position
        for _ in 0..left - 1 {
            left_tail = &mut left_tail.as_mut().unwrap().next;
        }

        // `start` will point to the first node of the sublist to be reversed
        let mut prev = left_tail.as_mut().unwrap().next.take();
        let mut curr = prev.as_mut().unwrap().next.take();

        // Reverse the sublist
        for _ in 0..right - left {
            let next = curr.as_mut().unwrap().next.take();
            curr.as_mut().unwrap().next = prev;
            prev = curr;
            curr = next;
        }

        // Reconnect the reversed sublist with the rest of the list
        left_tail.as_mut().unwrap().next = prev;
        let mut tail = left_tail;
        for _ in 0..right - left + 1 {
            tail = &mut tail.as_mut().unwrap().next;
        }
        tail.as_mut().unwrap().next = curr;

        dummy_head.unwrap().next
    }
}

fn main() {
    let head = create_linked_list(vec![1, 2, 3, 4, 5]);
    print_linked_list(head.clone());
    let new_head = Solution::reverse_between(head, 2, 4);
    print_linked_list(new_head);
}