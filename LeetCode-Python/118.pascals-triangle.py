# -*- encoding: utf-8 -*-
'''
@File    :   118.pascals-triangle.py
@Time    :   2019/11/18 11:39:54
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (48.58%)
# Likes:    921
# Dislikes: 84
# Total Accepted:    305K
# Total Submissions: 625.6K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
#
#
#

# @lc code=start


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            curr = [1, 1]
            for j in range(0, len(result[i-1])-1):
                curr.insert(1+j, result[i-1][j] + result[i-1][j+1])
            result.append(curr)
        return result
# @lc code=end
