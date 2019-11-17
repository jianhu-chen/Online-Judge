# -*- encoding: utf-8 -*-
'''
@File    :   69.sqrt-x.py
@Time    :   2019/11/17 20:54:46
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (32.36%)
# Likes:    948
# Dislikes: 1585
# Total Accepted:    441.4K
# Total Submissions: 1.4M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
#
# Example 1:
#
#
# Input: 4
# Output: 2
#
#
# Example 2:
#
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
# the decimal part is truncated, 2 is returned.
#
#
#

# @lc code=start


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x ** 0.5)
        # for i in range(x + 2):
        #     if i*i > x:
        #         return i - 1

# @lc code=end
