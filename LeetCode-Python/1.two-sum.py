# -*- encoding: utf-8 -*-
'''
@File    :   1.two-sum.py
@Time    :   2019/11/04 23:40:01
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (44.71%)
# Likes:    12345
# Dislikes: 433
# Total Accepted:    2.3M
# Total Submissions: 5.1M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            nums_copy = nums.copy()
            nums_copy.remove(n)
            try:
                j = nums_copy.index(target-n)
                return [i, j]
            except:
                pass
            

        
# @lc code=end
