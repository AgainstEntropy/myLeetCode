// 合并两个有序链表
// Merge Two Sorted Lists

use leetcode::common::{ListNode, create_linked_list, print_linked_list};

struct Solution {}

impl Solution {
    pub fn merge_two_lists(mut list1: Option<Box<ListNode>>, mut list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy_head = Some(Box::new(ListNode::new(0)));

        let mut curr = dummy_head.as_mut().unwrap();

        while list1.is_some() && list2.is_some() {
            if list1.as_ref().unwrap().val <= list2.as_ref().unwrap().val {
                curr.next = list1;
                list1 = curr.next.as_mut().unwrap().next.take();
            } else {
                curr.next = list2;
                list2 = curr.next.as_mut().unwrap().next.take();
            }
            curr = curr.next.as_mut().unwrap();
        }

        curr.next = list1.or(list2);

        dummy_head.unwrap().next
    }
}

fn main() {
    let arr1 = vec![1, 2, 4];
    let arr2 = vec![1, 3, 4];

    let list1 = create_linked_list(&arr1);
    let list2 = create_linked_list(&arr2);
    print_linked_list(&list1);
    print_linked_list(&list2);
    print_linked_list(&Solution::merge_two_lists(list1, list2));
}

