struct Solution;

impl Solution {
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        let n = grid.len();
        let m = grid[0].len();
        let mut islands = 0;

        let mut grid = grid;

        for i in 0..n {
            for j in 0..m {
                if grid[i][j] == '1' {
                    Self::dfs(i as i32, j as i32, n as i32, m as i32, &mut grid);
                    islands += 1;
                }
            }
        }

        islands
    }

    fn dfs(i: i32, j: i32, n: i32, m: i32, grid: &mut Vec<Vec<char>>) {
        if i < 0 || i >= n || j < 0 || j >= m || grid[i as usize][j as usize] == '0' {
            return;
        }
        grid[i as usize][j as usize] = '0';
        Self::dfs(i + 1, j, n, m, grid);
        Self::dfs(i - 1, j, n, m, grid);
        Self::dfs(i, j + 1, n, m, grid);
        Self::dfs(i, j - 1, n, m, grid);
    }
}

fn main() {
    let test_cases = vec![
        vec![
            vec!['1', '1', '1', '1', '0'],
            vec!['1', '1', '0', '1', '0'],
            vec!['1', '1', '0', '0', '0'],
            vec!['0', '0', '0', '0', '0'],
        ],
        vec![
            vec!['1', '1', '0', '0', '0'],
            vec!['1', '1', '0', '0', '0'],
            vec!['0', '0', '1', '0', '0'],
            vec!['0', '0', '0', '1', '1'],
        ],
    ];
    for case in test_cases {
        let res = Solution::num_islands(case);
        println!("{}", res);
    }
}
