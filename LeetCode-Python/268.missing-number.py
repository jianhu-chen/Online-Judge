# -*- encoding: utf-8 -*-
'''
@File    :   268.missing-number.py
@Time    :   2020/02/02 12:42:05
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=268 lang=python
#
# [268] Missing Number
#

# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """方法1：sort O(nlogn) and O(1)
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for idx in range(len(nums)):
            if nums[idx] != idx:
                return idx
        return len(nums)
    
    def missingNumber(self, nums):
        """方法2：hash table O(n) and O(n)
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                return i
    
    def missingNumber(self, nums):
            """方法3：XOR O(n) and O(1)
            :type nums: List[int]
            :rtype: int
            """
            result = len(nums)
            for idx, num in enumerate(nums):
                result ^= idx ^ num
            return result
# @lc code=end

