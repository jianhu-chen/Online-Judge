# -*- encoding: utf-8 -*-
'''
@File    :   350.intersection-of-two-arrays-ii.py
@Time    :   2020/02/05 23:40:25
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=350 lang=python
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for n in nums1:
            if n in nums2:
                nums2.remove(n)
                result.append(n)
        return result
# @lc code=end

