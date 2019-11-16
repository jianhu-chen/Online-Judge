# -*- encoding: utf-8 -*-
'''
@File    :   35.search-insert-position.py
@Time    :   2019/11/16 23:28:41
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (41.26%)
# Likes:    1627
# Dislikes: 207
# Total Accepted:    479.7K
# Total Submissions: 1.2M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
#
# Input: [1,3,5,6], 5
# Output: 2
#
#
# Example 2:
#
#
# Input: [1,3,5,6], 2
# Output: 1
#
#
# Example 3:
#
#
# Input: [1,3,5,6], 7
# Output: 4
#
#
# Example 4:
#
#
# Input: [1,3,5,6], 0
# Output: 0
#
#
#

# @lc code=start


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
# @lc code=end
