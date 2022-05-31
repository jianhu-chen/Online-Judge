#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (70.32%)
# Likes:    467
# Dislikes: 0
# Total Accepted:    50.2K
# Total Submissions: 71.4K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 示例:
# 
# 输入: 4
# 输出: [
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自
# 百度百科 - 皇后 ）
# 
# 
#

# @lc code=start
import copy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []

        def backtrack(row, track):
            # 结束条件
            if row == n:
                ret.append(track)

            for col in range(n):
                # 排除不合法的选择
                if not is_valid(row, col, track):
                    continue

                track_copy = copy.deepcopy(track)
                row_i_list = list(track_copy[row])
                row_i_list[col] = "Q"
                track_copy[row] = "".join(row_i_list)
                backtrack(row + 1, track_copy)

        def is_valid(row, col, track):
            # "|" 方向
            for i in range(n):
                if track[i][col] == "Q" and i != row:
                    return False

            # "\" 方向
            diff = row - col
            for i in range(n):
                j = i - diff
                if i in range(n) and j in range(n):
                    if track[i][j] == "Q" and (i, j) != (row, col):
                        return False

            # "/" 方向
            sum = row + col
            for i in range(n):
                j = sum - i
                if i in range(n) and j in range(n):
                    if track[i][j] == "Q" and (i, j) != (row, col):
                        return False

            return True

        init = ["." * n for _ in range(n)]
        backtrack(0, init)
        return ret
# @lc code=end

