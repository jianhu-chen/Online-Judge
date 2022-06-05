#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (28.64%)
# Likes:    2402
# Dislikes: 0
# Total Accepted:    282K
# Total Submissions: 983.1K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#

# @lc code=start
import copy


class Solution:
    def twoSum(self, nums, target=0):
        ret = []
        # O(Nlog(N))
        nums = sorted(nums)
        left, right = 0, len(nums) - 1
        # O(N)
        while left < right:
            left_val, right_val = nums[left], nums[right]
            sum = left_val + right_val
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            elif sum == target:
                ret.append([left_val, right_val])
                while left < right and left_val == nums[left]:
                    left += 1
                while left < right and right_val == nums[right]:
                    right -= 1
        return ret

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        ret = []
        nums = sorted(nums)
        idx = 0
        while idx < len(nums):
            num = nums[idx]
            target = 0 - num
            two_sum_ret = self.twoSum(nums[idx + 1:], target=target)
            for r in two_sum_ret:
                ret.append([num] + r)
            while idx < len(nums) and nums[idx] == num:
                idx += 1
        return ret

# @lc code=end
