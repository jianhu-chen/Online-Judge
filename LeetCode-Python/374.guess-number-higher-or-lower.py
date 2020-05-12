# -*- encoding: utf-8 -*-
'''
@File    :   374.guess-number-higher-or-lower.py
@Time    :   2020/05/13 00:43:52
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=374 lang=python
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left < right:
            center = (left + right + 1) // 2
            response = guess(center)
            if response == 1:
                left = center
            elif response == -1:
                right = center
            else:
                return center
        return left

# @lc code=end
