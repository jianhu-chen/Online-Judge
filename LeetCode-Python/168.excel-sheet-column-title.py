# -*- encoding: utf-8 -*-
'''
@File    :   168.excel-sheet-column-title.py
@Time    :   2019/11/21 16:55:28
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=168 lang=python
#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (29.79%)
# Likes:    875
# Dislikes: 180
# Total Accepted:    191.1K
# Total Submissions: 640.3K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
#
# For example:
#
#
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB
# ⁠   ...
#
#
# Example 1:
#
#
# Input: 1
# Output: "A"
#
#
# Example 2:
#
#
# Input: 28
# Output: "AB"
#
#
# Example 3:
#
#
# Input: 701
# Output: "ZY"
#
#

# @lc code=start


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        capitals = [chr(_) for _ in range(ord('A'), ord('Z') + 1)]
        result = ''
        while n:
            result = capitals[(n - 1) % 26] + result
            n = (n - 1) // 26
        return result

# @lc code=end


print(Solution().convertToTitle(28))
