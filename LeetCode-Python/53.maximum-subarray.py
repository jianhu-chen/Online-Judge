# -*- encoding: utf-8 -*-
'''
@File    :   53.maximum-subarray.py
@Time    :   2019/11/17 13:19:00
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (44.97%)
# Likes:    5496
# Dislikes: 234
# Total Accepted:    687.8K
# Total Submissions: 1.5M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
#
#

# @lc code=start

# 解法1：动态规划
# 1. 描述问题的最优解结构特征
# 设 f(i) 表示以第 i 个数字结尾的连续子数组的最大和，则我们最终要求的答案是:
#       max( f(i) )  0<=i<=n-1
# 2. 递归定义最优解值
#       f(i) = max( f(i-1) + nums[i], nums[i])
# 3. 自底向上计算最优解值
#       f(0) = nums[0]


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_sum = nums[0]
        cur_sum = nums[0]
        for n in nums[1:]:
            cur_sum = max(cur_sum + n, n)
            max_sum = max(cur_sum, max_sum)

        return max_sum

# @lc code=end


if __name__ == "__main__":
    print(Solution().maxSubArray(
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]))
