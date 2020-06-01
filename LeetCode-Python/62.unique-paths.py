# -*- encoding: utf-8 -*-
'''
@File    :   62.unique-paths.py
@Time    :   2020/06/01 01:02:45
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

# @lc code=start


class Solution(object):
    def uniquePaths(self, m, n):
        """
        方法1: 递归, 超时
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

    def uniquePaths(self, m, n):
        """
        方法2: 动态规划
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]

    def uniquePaths(self, m, n):
        """
        方法3: 动态规划
        空间复杂度O(min(m, n))
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1]
        return dp[-1]
# @lc code=end


if __name__ == "__main__":
    print(Solution().uniquePaths(2, 4))
