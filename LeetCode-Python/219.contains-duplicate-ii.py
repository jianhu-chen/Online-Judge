# -*- encoding: utf-8 -*-
'''
@File    :   219.contains-duplicate-ii.py
@Time    :   2020/01/31 16:48:27
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=219 lang=python
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_table = dict()
        for idx, n in enumerate(nums):
            if n not in hash_table:
                hash_table[n] = idx
            else:
                if idx - hash_table[n] <= k:
                    return True
                else:
                    hash_table[n] = idx
        return False
        
# @lc code=end

