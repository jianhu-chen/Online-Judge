/*
 * @lc app=leetcode.cn id=51 lang=cpp
 *
 * [51] N皇后
 *
 * https://leetcode-cn.com/problems/n-queens/description/
 *
 * algorithms
 * Hard (70.32%)
 * Likes:    467
 * Dislikes: 0
 * Total Accepted:    50.2K
 * Total Submissions: 71.4K
 * Testcase Example:  '4'
 *
 * n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
 * 
 * 
 * 
 * 上图为 8 皇后问题的一种解法。
 * 
 * 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
 * 
 * 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
 * 
 * 示例:
 * 
 * 输入: 4
 * 输出: [
 * ⁠[".Q..",  // 解法 1
 * ⁠ "...Q",
 * ⁠ "Q...",
 * ⁠ "..Q."],
 * 
 * ⁠["..Q.",  // 解法 2
 * ⁠ "Q...",
 * ⁠ "...Q",
 * ⁠ ".Q.."]
 * ]
 * 解释: 4 皇后问题存在两个不同的解法。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 
 * 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自
 * 百度百科 - 皇后 ）
 * 
 * 
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution
{
public:
    void backtrack(vector<string> track, int n)
    {
        // 判断是否满足结束条件
        if (track.size() == n)
        {
            ret.push_back(track);
        }

        // 做选择
        for (int col = 0; col < n; ++col)
        {
            string line(n - 1, '.');
            line.insert(col, "Q");
            track.push_back(line);
            int row = track.size() - 1;
            if (isValid(track, row, col))
            {
                backtrack(track, n);
            }
            track.pop_back();
        }
    }

    bool isValid(vector<string> track, int row, int col)
    {
        // "|" 方向
        for (int i = 0; i < row; ++i)
        {
            if (track[i][col] == 'Q')
            {
                return false;
            }
        }

        // "/" 方向
        int diff = row - col;
        for (int i = 0; i < row; ++i)
        {
            int j = i - diff;
            if (j >= 0 && track[i][j] == 'Q')
            {
                return false;
            }
        }

        // "\" 方向
        int sum = row + col;
        for (int i = 0; i < row; ++i)
        {
            int j = sum - i;
            if (j >= 0 && track[i][j] == 'Q')
            {
                return false;
            }
        }
        return true;
    }

    vector<vector<string>> solveNQueens(int n)
    {
        vector<string> track;
        backtrack(track, n);
        return ret;
    }

private:
    vector<vector<string>> ret;
};
// @lc code=end
