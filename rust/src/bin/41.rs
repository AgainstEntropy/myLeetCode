// 缺失的第一个正整数
// First Missing Positive

struct Solution {}

impl Solution {
    pub fn first_missing_positive(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        let n = nums.len();
        for i in 0..n {
            while (1 <= nums[i] && nums[i] <= n as i32) && (nums[i] != nums[nums[i] as usize - 1]) {
                let idx = nums[i] as usize - 1;
                nums.swap(i, idx);
            }
        }

        for i in 0..n {
            let expected = (i + 1) as i32;
            if nums[i] != expected {
                return expected;
            }
        }

        return (n + 1) as i32;
    }
}

fn main() {
    let test_cases = vec![
        (vec![1, 2, 0],),
        (vec![3, 4, -1, 1],),
        (vec![7, 8, 9, 11, 12],),
        (vec![1],),
        (vec![2],),
    ];

    for case in test_cases {
        println!("{:?}", Solution::first_missing_positive(case.0));
    }
}


