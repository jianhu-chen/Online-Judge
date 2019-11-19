# -*- encoding: utf-8 -*-
'''
@File    :   136.single-number.py
@Time    :   2019/11/19 23:11:59
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (61.90%)
# Likes:    3059
# Dislikes: 119
# Total Accepted:    567.4K
# Total Submissions: 914.5K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,1]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,1,2,1,2]
# Output: 4
#
#
#

# @lc code=start


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法1 O(n)
        # return 2*sum(set(nums)) - sum(nums)

        # 方法2 O(n)
        dic = {}
        for n in nums:
            try:
                dic.pop(n)
            except:
                dic[n] = 1
        return dic.popitem()[0]
# @lc code=end
