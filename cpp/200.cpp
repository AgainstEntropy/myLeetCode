// 岛屿数量
// Number of Islands

#include "common.h"

class Solution
{
public:
    int numIslands(std::vector<std::vector<char>> &grid)
    {
        int n = grid.size();
        int m = grid[0].size();
        int islands = 0;

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (grid[i][j] == '1')
                {
                    dfs(i, j, n, m, grid);
                    islands++;
                }
            }
        }
        return islands;
    }

    void dfs(int i, int j, int n, int m, std::vector<std::vector<char>> &grid)
    {
        if (i < 0 || i >= n || j < 0 || j >= m || grid[i][j] == '0')
        {
            return;
        }
        grid[i][j] = '0';
        dfs(i + 1, j, n, m, grid);
        dfs(i - 1, j, n, m, grid);
        dfs(i, j + 1, n, m, grid);
        dfs(i, j - 1, n, m, grid);
    }
};

int main()
{
    std::vector<std::vector<std::vector<char>>> test_cases = {
        {{'1', '1', '1', '1', '0'},
         {'1', '1', '0', '1', '0'},
         {'1', '1', '0', '0', '0'},
         {'0', '0', '0', '0', '0'}},
        {{'1', '1', '0', '0', '0'},
         {'1', '1', '0', '0', '0'},
         {'0', '0', '1', '0', '0'},
         {'0', '0', '0', '1', '1'}}};

    Solution sol;
    for (auto &test_case : test_cases)
    {
        int res = sol.numIslands(test_case);
        std::cout << res << std::endl;
    }
}
