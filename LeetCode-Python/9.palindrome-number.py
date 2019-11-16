# -*- encoding: utf-8 -*-
'''
@File    :   9.palindrome-number.py
@Time    :   2019/11/16 16:48:08
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (45.47%)
# Likes:    1723
# Dislikes: 1417
# Total Accepted:    727.2K
# Total Submissions: 1.6M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
#
# Example 1:
#
#
# Input: 121
# Output: true
#
#
# Example 2:
#
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Follow up:
#
# Coud you solve it without converting the integer to a string?
#
#

# @lc code=start


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        x_copy = x
        reversed_x = 0
        while x:
            reversed_x = reversed_x * 10 + x % 10
            x /= 10

        if x_copy == reversed_x:
            return True
        else:
            return False

# @lc code=end
