#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (40.42%)
# Likes:    705
# Dislikes: 0
# Total Accepted:    106K
# Total Submissions: 262.2K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
#
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
#
# 示例 2:
#
# 输入: coins = [2], amount = 3
# 输出: -1
#
#
#
# 说明:
# 你可以认为每种硬币的数量是无限的。
#
#

# @lc code=start
class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        备忘录
        """
        mem = dict()

        def dp(amount):
            if amount == 0:
                return 0
            elif amount < 0:
                return -1

            if amount in mem:
                return mem[amount]

            ret = float("INF")
            for coin in coins:
                subproblem = dp(amount - coin)
                if subproblem == -1:
                    continue
                ret = min(ret, subproblem + 1)

            mem[amount] = ret if ret != float("INF") else -1

            return mem[amount]

        return dp(amount)

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        动态规划
        """
        if amount == 0:
            return 0
        elif amount < 0:
            return -1

        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for amount_i in range(1, amount + 1):
            for coin in coins:
                if amount_i - coin < 0:
                    continue
                dp[amount_i] = min(dp[amount_i], dp[amount_i - coin] + 1)

        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
# @lc code=end
