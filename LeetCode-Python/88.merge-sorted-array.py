# -*- encoding: utf-8 -*-
'''
@File    :   88.merge-sorted-array.py
@Time    :   2019/11/17 21:33:59
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (37.29%)
# Likes:    1416
# Dislikes: 3247
# Total Accepted:    447.2K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
#
# Note:
#
#
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
#
#
# Example:
#
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
#
#

# @lc code=start


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while j < n:
            while i < m and nums1[i] < nums2[j]:
                i += 1
            nums1.insert(i, nums2[j])
            m += 1
            j += 1

        del nums1[m:]


# @lc code=end
Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
