# -*- encoding: utf-8 -*-
'''
@File    :   121.best-time-to-buy-and-sell-stock.py
@Time    :   2019/11/18 11:51:11
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (48.61%)
# Likes:    3411
# Dislikes: 154
# Total Accepted:    638.4K
# Total Submissions: 1.3M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
#
#
# Example 2:
#
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
#
#

# @lc code=start
# 我们可以维持两个变量——minprice 和 maxprofit，
# 它们分别对应迄今为止所得到的最小的谷值和最大的利润
# （卖出价格与最低价格之间的最大差值）。


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = 9999
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            if p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit


# @lc code=end
