# -*- encoding: utf-8 -*-
'''
@File    :   172.factorial-trailing-zeroes.py
@Time    :   2019/11/21 16:55:52
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=172 lang=python
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (37.64%)
# Likes:    586
# Dislikes: 835
# Total Accepted:    177.9K
# Total Submissions: 472.8K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
#
# Example 1:
#
#
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
#
# Example 2:
#
#
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
#
# Note: Your solution should be in logarithmic time complexity.
#
#

# @lc code=start


class Solution(object):
    # def trailingZeroes(self, n):
    #     """方法一：暴力法 超时
    #     :type n: int
    #     :rtype: int
    #     """
    #     mul = 1
    #     for i in range(1, n+1):
    #         mul *= i
    #     count = 0
    #     while mul:
    #         if mul % 10 == 0:
    #             count += 1
    #         else:
    #             break
    #         mul = int(mul / 10)
    #     return count

    def trailingZeroes(self, n):
        """方法二：除5法 log_5n
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n / 5
            n /= 5
        return count

# 0的来源 2 * 5 所以一对2和5即可产生一个0, 所以0的个数即为min(阶乘中5的个数和2的个数)
# 又因为是2的倍数的数一定比是5的倍数的数多 所以2的个数一定>=5的个数 所以只需要统计 5 的个数了
# 例如 5！ = 1 * 2 * 3 * 4 * 5
# 2 2 2 5  一个2和一个5配对出现0 所以5!末尾只有一个零
# 而在 n = 25 时 可以产生5的有 5 10 15 20 25
# 即 n/5 = 5个 然鹅 25 = 5*5 所以少算了一个5
# n>=25时,故而需要补上 因此所有可以产生25的也要加上
# 即为 n/5 + n/25  然鹅 625 = 25*25 所以又少算了一个25
# 继续补上...
# 所以最终为 n/5 + n/25 + n/625 +...
# 即 n/5 + n/5/5 + n/5/5/5 + ...
# @lc code=end


print(Solution().trailingZeroes(7))
