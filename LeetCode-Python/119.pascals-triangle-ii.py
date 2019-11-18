# -*- encoding: utf-8 -*-
'''
@File    :   119.pascals-triangle-ii.py
@Time    :   2019/11/18 11:48:42
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=119 lang=python
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (45.76%)
# Likes:    577
# Dislikes: 182
# Total Accepted:    235.2K
# Total Submissions: 512.3K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the k^th index row of the
# Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 3
# Output: [1,3,3,1]
#
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#
#

# @lc code=start


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        result = [[1], [1, 1]]
        for i in range(2, rowIndex+1):
            curr = [1, 1]
            for j in range(0, len(result[i-1])-1):
                curr.insert(1+j, result[i-1][j] + result[i-1][j+1])
            result.append(curr)
        return result[-1]
# @lc code=end
