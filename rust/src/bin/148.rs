// 排序链表
// Sort List

use leetcode::common::{ListNode, create_linked_list, print_linked_list};

struct Solution {}

impl Solution {
    pub fn sort_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none() || head.as_ref().unwrap().next.is_none() {
            return head;
        }

        let (left, right) = Self::split(head);

        Self::merge(Self::sort_list(left), Self::sort_list(right))
    }

    fn split(head: Option<Box<ListNode>>) -> (Option<Box<ListNode>>, Option<Box<ListNode>>) {
        // Handle empty list or single node
        if head.is_none() || head.as_ref().unwrap().next.is_none() {
            return (head, None);
        }

        let mut slow = head.as_ref();
        let mut fast = head.as_ref().unwrap().next.as_ref();

        while fast.is_some() && fast.unwrap().next.is_some() {
            slow = slow.unwrap().next.as_ref();
            fast = fast.unwrap().next.as_ref().unwrap().next.as_ref();
        }

        let right = slow.unwrap().next.clone();
        let mut left = head;

        // here we need a mutable pointer to cut off the left part
        let mut slow_mut = left.as_mut().unwrap();
        while slow_mut.next.is_some() && slow_mut.next.as_ref() != right.as_ref() {
            slow_mut = slow_mut.next.as_mut().unwrap();
        }
        slow_mut.next = None;

        (left, right)
    }

    fn merge(mut left: Option<Box<ListNode>>, mut right: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy_head = ListNode::new(0);
        let mut curr = &mut dummy_head;

        while left.is_some() && right.is_some() {
            if left.as_ref().unwrap().val <= right.as_ref().unwrap().val {
                let next = left.clone().unwrap().next.take();
                curr.next = left;
                left = next;
            } else {
                let next = right.clone().unwrap().next.take();
                curr.next = right;
                right = next;
            }
            curr = curr.next.as_mut().unwrap();
        }

        curr.next = left.or(right);

        dummy_head.next
    }
}

fn main() {
    let head = create_linked_list(vec![-1, 5, 3, 4, 0]);
    print_linked_list(&head);
    print_linked_list(&Solution::sort_list(head));
}
