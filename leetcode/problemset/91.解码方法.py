#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (23.99%)
# Likes:    440
# Dislikes: 0
# Total Accepted:    56.5K
# Total Submissions: 235.5K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 
# 示例 1:
# 
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
# 
# 示例 2:
# 
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# 
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
