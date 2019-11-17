# -*- encoding: utf-8 -*-
'''
@File    :   66.plus-one.py
@Time    :   2019/11/17 13:36:24
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (41.74%)
# Likes:    1067
# Dislikes: 1846
# Total Accepted:    470.5K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
#
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
#
# Example 1:
#
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
#
# Example 2:
#
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#
#

# @lc code=start


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        digits[-1] += 1
        for i in range(-1, -len(digits)-1, -1):
            if digits[i] >= 10:
                digits[i] %= 10
                try:
                    digits[i-1] += 1
                except:
                    digits.insert(0, 1)

        return digits
# @lc code=end


print(Solution().plusOne([9]))
