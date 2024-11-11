// 二叉树的中序遍历
// Binary Tree Inorder Traversal

use leetcode::common::{Rc, RefCell, TreeNode, create_binary_tree, NULL_VALUE};

struct Solution {}

impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut result = Vec::new();

        fn visit(node: &Option<Rc<RefCell<TreeNode>>>, result: &mut Vec<i32>) {
            if node.is_none() {
                return;
            }
            visit(&node.as_ref().unwrap().borrow().left, result);
            result.push(node.as_ref().unwrap().borrow().val);
            visit(&node.as_ref().unwrap().borrow().right, result);
        }

        visit(&root, &mut result);
        result
    }
}

fn main() {
    let test_cases = vec![
        vec![1, NULL_VALUE, 2, 3],
        vec![1, 2, 3, 4, 5, NULL_VALUE, 8, NULL_VALUE, NULL_VALUE, 6, 7, 9],
    ];

    for case in test_cases {
        let root = create_binary_tree(&case);
        println!("{:?}", Solution::inorder_traversal(root));
    }
}
