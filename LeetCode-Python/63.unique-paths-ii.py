# -*- encoding: utf-8 -*-
'''
@File    :   63.unique-paths-ii.py
@Time    :   2020/06/02 00:15:43
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=63 lang=python
#
# [63] Unique Paths II
#

# @lc code=start


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    dp[i][j] = 1 if obstacleGrid[i][j] == 0 else 0
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1] if obstacleGrid[i][j] == 0 else 0
                elif j == 0 and i != 0:
                    dp[i][j] = dp[i-1][j] if obstacleGrid[i][j] == 0 else 0
                else:
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]

# @lc code=end


if __name__ == "__main__":
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(
        Solution().uniquePathsWithObstacles(obstacleGrid)
    )
