# -*- encoding: utf-8 -*-
'''
@File    :   7.reverse-integer.py
@Time    :   2019/11/04 23:40:21
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.53%)
# Likes:    2561
# Dislikes: 4007
# Total Accepted:    852.4K
# Total Submissions: 3.3M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
#
#

# @lc code=start


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0

        if x < 0:
            is_negtive = True
            x = - x
        else:
            is_negtive = False

        while x:
            unit = x % 10
            x /= 10
            result = result * 10 + unit
            if result < -2 ** 31 or result >= 2 ** 31:
                return 0

        if is_negtive:
            result = - result
        return result

# @lc code=end
