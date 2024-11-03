// Definition for singly-linked list.

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

pub fn create_linked_list(arr: Vec<i32>) -> Option<Box<ListNode>> {
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
