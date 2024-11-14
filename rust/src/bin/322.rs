// 零钱兑换
// Coin Change

struct Solution;

impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let mut min_coins = vec![-1; amount as usize + 1];
        min_coins[0] = 0;
        let mut coins = coins;
        coins.sort();

        for i in 0..=amount as usize {
            for &c in &coins {
                if i as i32 + c <= amount && min_coins[i] != -1 {
                    if min_coins[i + c as usize] == -1 || min_coins[i + c as usize] > min_coins[i] + 1 {
                        min_coins[i + c as usize] = min_coins[i] + 1;
                    }
                }
            }
        }
        min_coins[amount as usize]
    }
}

fn main() {
    let test_cases = vec![
        (vec![1, 2, 5], 11),
        (vec![2], 3),
        (vec![1], 0),
    ];

    for (coins, amount) in test_cases {
        println!("{}", Solution::coin_change(coins, amount));
    }
}
