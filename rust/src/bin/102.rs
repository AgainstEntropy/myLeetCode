// 二叉树的层序遍历
// Binary Tree Level Order Traversal

use leetcode::common::{Vec,Rc, RefCell, TreeNode, NULL_VALUE, create_binary_tree};

struct Solution;

impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut result = vec![];
        if root.is_none() {
            return result;
        }

        let mut queue = Vec::new();
        queue.push((root, 0));

        while !queue.is_empty() {
            let (node, level) = queue.remove(0);
            if node.is_none() {
                continue;
            }
            if level >= result.len() {
                result.push(vec![]);
            }
            result[level].push(node.as_ref().unwrap().borrow().val);
            queue.push((node.as_ref().unwrap().borrow().left.clone(), level + 1));
            queue.push((node.as_ref().unwrap().borrow().right.clone(), level + 1));
        }

        result
    }
}

fn main() {
    let test_cases = vec![
        vec![3, 9, 20, NULL_VALUE, NULL_VALUE, 15, 7],
        vec![1],
        vec![],
    ];

    for test_case in test_cases {
        let root = create_binary_tree(&test_case);
        let result = Solution::level_order(root);
        println!("{:?}", result);
    }
}
