// Definition for singly-linked list.

pub use std::{cell::RefCell, rc::Rc};
pub use std::vec::Vec;

//
// Linked List
//
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
  #[inline]
  pub fn new(val: i32) -> Self {
        ListNode { next: None, val }
  }
}

pub fn create_linked_list(arr: &Vec<i32>) -> Option<Box<ListNode>> {
    if arr.is_empty() {
        return None;
    }
    let mut head: Option<Box<ListNode>> = Some(Box::new(ListNode::new(arr[0])));
    let mut node: &mut Box<ListNode> = head.as_mut().unwrap();
    for &val in arr[1..].iter() {
        node.next = Some(Box::new(ListNode::new(val)));
        node = node.next.as_mut().unwrap();
    }
    head
}

pub fn print_linked_list(head: &Option<Box<ListNode>>) {
    let mut node = head;
    while let Some(n) = node {
        print!("{} -> ", n.val);
        node = &n.next;
    }
    println!("None");
}

//
// Binary Tree
//
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

pub const NULL_VALUE: i32 = -1;

pub fn create_binary_tree(arr: &Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
    use std::collections::VecDeque;

    if arr.is_empty() {
        return None;
    }

    let root = Rc::new(RefCell::new(TreeNode::new(arr[0])));
    let mut queue = VecDeque::new();
    queue.push_back(Rc::clone(&root));
    let mut i = 1;

    while i < arr.len() {
        let current = queue.pop_front().unwrap();

        // Left child
        if arr[i] != NULL_VALUE {
            let left_node = Rc::new(RefCell::new(TreeNode::new(arr[i])));
            current.borrow_mut().left = Some(Rc::clone(&left_node));
            queue.push_back(left_node);
        }
        i += 1;

        // Right child
        if i < arr.len() {
            if arr[i] != NULL_VALUE {
                let right_node = Rc::new(RefCell::new(TreeNode::new(arr[i])));
                current.borrow_mut().right = Some(Rc::clone(&right_node));
                queue.push_back(right_node);
            }
            i += 1;
        }
    }

    Some(root)
}
