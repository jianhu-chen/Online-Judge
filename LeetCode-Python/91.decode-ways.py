# -*- encoding: utf-8 -*-
'''
@File    :   91.decode-ways.py
@Time    :   2020/06/03 01:02:10
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """方法1: 动态规划
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0
        if s[0] == "0":
            return 0

        dp = [0 for _ in range(length)]
        dp[0] = 1
        # 两种情况:
        # 1. s[i] != "0", 可以将s[i]单独解码
        # 2. s[i-1: i+1] in [10, 26], 可以将s[i-1: i+1]单独解码成一个数字
        #    特殊情况是当 i == 1 时, 情况特殊, 单独考虑
        for i in range(1, length):
            if s[i] != "0":
                dp[i] = dp[i-1]
            if 10 <= int(s[i-1: i+1]) <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]
        return dp[-1]
# @lc code=end
