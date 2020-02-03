# -*- encoding: utf-8 -*-
'''
@File    :   303.range-sum-query-immutable.py
@Time    :   2020/02/03 15:08:59
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=303 lang=python
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
# class NumArray(object):

#     def __init__(self, nums):
#         """方法1：暴力
#         :type nums: List[int]
#         """
#         self.nums = nums

#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         return sum(self.nums[i: j+1])

class NumArray(object):

    def __init__(self, nums):
        """方法2：优化多次调用
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = dict()
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if (i, j+1) not in self.sums:
            self.sums[(i, j+1)] = sum(self.nums[i: j+1])
        return self.sums[(i, j+1)]
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    r = NumArray(nums).sumRange(0, 2)
    print(r)
