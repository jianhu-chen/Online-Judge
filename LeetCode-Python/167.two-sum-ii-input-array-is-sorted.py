# -*- encoding: utf-8 -*-
'''
@File    :   167.two-sum-ii-input-array-is-sorted.py
@Time    :   2019/11/21 12:54:53
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input array is sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (51.73%)
# Likes:    1164
# Dislikes: 471
# Total Accepted:    312K
# Total Submissions: 601.6K
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers that is already sorted in ascending order, find
# two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they
# add up to the target, where index1 must be less than index2.
#
# Note:
#
#
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.
#
#
# Example:
#
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
#
#

# @lc code=start


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = dict()
        for i, n in enumerate(numbers):
            try:
                j = hash_map.pop(target - n)
                return [j + 1, i + 1]
            except:
                hash_map[n] = i

# @lc code=end
