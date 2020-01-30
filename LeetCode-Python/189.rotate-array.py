# -*- encoding: utf-8 -*-
'''
@File    :   189.rotate-array.py
@Time    :   2020/01/30 19:42:41
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return
        for i in range(k):
            nums.insert(0, nums.pop())
# @lc code=end

