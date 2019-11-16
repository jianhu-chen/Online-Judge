# -*- encoding: utf-8 -*-
'''
@File    :   26.remove-duplicates-from-sorted-array.py
@Time    :   2019/11/16 17:45:26
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (42.35%)
# Likes:    1825
# Dislikes: 3992
# Total Accepted:    736.8K
# Total Submissions: 1.7M
# Testcase Example:  '[1,1,2]'
#
# Given a sorted array nums, remove the duplicates in-place such that each
# element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
#
# Example 1:
#
#
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums
# being 1 and 2 respectively.
#
# It doesn't matter what you leave beyond the returned length.
#
# Example 2:
#
#
# Given nums = [0,0,1,1,1,2,2,3,3,4],
#
# Your function should return length = 5, with the first five elements of nums
# being modified to 0, 1, 2, 3, and 4 respectively.
#
# It doesn't matter what values are set beyond the returned length.
#
#
# Clarification:
#
# Confused why the returned value is an integer but your answer is an array?
#
# Note that the input array is passed in by reference, which means modification
# to the input array will be known to the caller as well.
#
# Internally you can think of this:
#
#
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len
# elements.
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
#

# @lc code=start


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        pre = nums[0]  # 上一个已出现的数值
        i = 1
        j = 1  # 待交换的位置下标
        while i < len(nums):
            if nums[i] != pre:
                pre = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1
        del nums[j:]
        return j

# @lc code=end


Solution().removeDuplicates([1, 1, 2])
