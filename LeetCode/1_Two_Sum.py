# -*- coding: utf-8 -*-
# @File 	: 1_Two_Sum.py
# @Author 	: jianhuChen
# @Date 	: 2019-01-21 11:38:55
# @License 	: Copyright(C), USTC
# @Last Modified by  : jianhuChen
# @Last Modified time: 2019-01-21 18:45:39

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i, j]
        return None
