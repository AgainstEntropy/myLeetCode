// 无重复字符的最长子串
// Longest Substring Without Repeating Characters

struct Solution;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let n = s.len();
        let mut left = 0;
        let mut right = 0;
        let mut max_len = 0;

        let mut chars: std::collections::HashMap<char, i32> = std::collections::HashMap::new();

        while right < n {
            let c_right = s.chars().nth(right).unwrap();
            *chars.entry(c_right).or_insert(0) += 1;
            while *chars.get(&c_right).unwrap() > 1 {
                let c_left = s.chars().nth(left).unwrap();
                *chars.get_mut(&c_left).unwrap() -= 1;
                left += 1;
            }
            max_len = max_len.max(right - left + 1);
            right += 1;
        }

        max_len as i32
    }
}

fn main() {
    let test_cases = vec![
        ("abcabcbb".to_string(),),
        ("bbbbb".to_string(),),
        ("pwwkew".to_string(),),
        ("".to_string(),),
    ];

    for (s, ) in test_cases {
        let res = Solution::length_of_longest_substring(s.clone());
        println!("{} -> {}", s, res);
    }
}

