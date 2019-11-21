# -*- encoding: utf-8 -*-
'''
@File    :   171.excel-sheet-column-number.py
@Time    :   2019/11/21 16:55:01
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=171 lang=python
#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (52.63%)
# Likes:    689
# Dislikes: 125
# Total Accepted:    248.3K
# Total Submissions: 471K
# Testcase Example:  '"A"'
#
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
#
# For example:
#
#
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28
# ⁠   ...
#
#
# Example 1:
#
#
# Input: "A"
# Output: 1
#
#
# Example 2:
#
#
# Input: "AB"
# Output: 28
#
#
# Example 3:
#
#
# Input: "ZY"
# Output: 701
#
#

# @lc code=start


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)):
            result += (ord(s[len(s) - i - 1]) - ord('A') + 1) * 26 ** i
        return result
# @lc code=end
