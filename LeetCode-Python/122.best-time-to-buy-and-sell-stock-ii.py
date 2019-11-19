# -*- encoding: utf-8 -*-
'''
@File    :   122.best-time-to-buy-and-sell-stock-ii.py
@Time    :   2019/11/19 23:19:34
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Easy (53.50%)
# Likes:    1381
# Dislikes: 1459
# Total Accepted:    400.1K
# Total Submissions: 746.1K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times).
#
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
#
# Example 1:
#
#
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit =
# 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 =
# 3.
#
#
# Example 2:
#
#
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
#
#
# Example 3:
#
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
#

# @lc code=start
# 如果我们跳过 peak_ipeak i 和 valley_j
# 试图通过考虑差异较大的点以获取更多的利润，
# 获得的净利润总是会小与包含它们而获得的静利润，
# 因为 C 总是小于 A+B。


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0
        # valley = prices[0]
        # peak = prices[0]
        # i = 0
        # while i < len(prices) - 1:
        #     while i < len(prices) - 1 and prices[i] >= prices[i+1]:
        #         i += 1
        #     valley = prices[i]
        #     while i < len(prices) - 1 and prices[i] <= prices[i+1]:
        #         i += 1
        #     peak = prices[i]
        #     max_profit += peak - valley
        # return max_profit

        # 方法二：
        # A+B+C 的和等于差值 D 所对应的连续峰和谷的高度之差。
        i = 0
        while i < len(prices) - 1:
            if prices[i] < prices[i+1]:
                max_profit += prices[i+1] - prices[i]
            i += 1
        return max_profit

# @lc code=end
