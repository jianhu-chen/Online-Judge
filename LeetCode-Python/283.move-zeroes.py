# -*- encoding: utf-8 -*-
'''
@File    :   283.move-zeroes.py
@Time    :   2020/02/02 14:05:55
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_idx = []
        for idx, n in enumerate(nums):
            if n == 0:
                zero_idx.append(idx)
        for i, idx in enumerate(zero_idx):
            nums.append(nums.pop(idx - i))

# @lc code=end

