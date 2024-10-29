// Longest Palindromic Subsequence
// 最长回文子序列


struct Solution {}

impl Solution {
    pub fn longest_palindrome_subseq(s: String) -> i32 {
        let n = s.len();
        let chars = s.chars().collect::<Vec<char>>();

        let mut m = vec![vec![0; n]; n];
        for i in 0..n {
            m[i][i] = 1;
        }

        for i in 1..n {
            for j in 0..n-i {
                if chars[j] == chars[j + i] {
                    m[j][j + i] = m[j + 1][j + i - 1] + 2;
                } else {
                    m[j][j + i] = std::cmp::max(m[j + 1][j + i], m[j][j + i - 1]);
                }
            }
        }

        m[0][n - 1]
    }
}

fn main() {
    assert_eq!(Solution::longest_palindrome_subseq("bbbab".to_string()), 4);
    assert_eq!(Solution::longest_palindrome_subseq("cbbd".to_string()), 2);
}