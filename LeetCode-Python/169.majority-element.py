# -*- encoding: utf-8 -*-
'''
@File    :   169.majority-element.py
@Time    :   2019/11/21 16:55:12
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (54.68%)
# Likes:    2139
# Dislikes: 184
# Total Accepted:    463.1K
# Total Submissions: 844.4K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
#
#

# @lc code=start


class Solution(object):
    # def majorityElement(self, nums):
    #     """方法一：哈希表 O(n)
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     hash_map = {}
    #     for n in nums:
    #         if n in hash_map:
    #             hash_map[n] += 1
    #         else:
    #             hash_map[n] = 1

    #     for key, val in hash_map.items():
    #         if val > len(nums) / 2:
    #             return key

    # def majorityElement(self, nums):
    #     """方法二：排序O(nlogn)
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     nums = sorted(nums)
    #     return nums[len(nums)//2]

    def majorityElement(self, nums):
        """方法三：投票法O(n)
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for n in nums:
            if count == 0:
                candidate = n
            if n == candidate:
                count += 1
            else:
                count -= 1
        return candidate
# @lc code=end
