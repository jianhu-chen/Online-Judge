#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (38.02%)
# Likes:    519
# Dislikes: 0
# Total Accepted:    92.6K
# Total Submissions: 243.6K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 
# 注意：
# 
# 答案中不可以包含重复的四元组。
# 
# 示例：
# 
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#

# @lc code=start
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

    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 3:
            return []

        ret = []
        nums = sorted(nums)
        idx = 0
        while idx < len(nums):
            num = nums[idx]
            two_sum_ret = self.twoSum(nums[idx + 1:], target=target - num)
            for r in two_sum_ret:
                ret.append([num] + r)
            while idx < len(nums) and nums[idx] == num:
                idx += 1
        return ret

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 方法一：
        # if len(nums) < 4:
        #     return []

        # ret = []
        # nums = sorted(nums)
        # idx = 0
        # while idx < len(nums):
        #     num = nums[idx]
        #     three_sum_ret = self.threeSum(nums[idx + 1:], target=target - num)
        #     for r in three_sum_ret:
        #         ret.append([num] + r)
        #     while idx < len(nums) and nums[idx] == num:
        #         idx += 1
        # return ret

        # 方法2：更抽象，可以求nSum
        nums = sorted(nums)  
        return self.nSum(nums, target, n=4)

    def nSum(self, nums: List[int], target: int, n: int) -> List[List[int]]:
        """
        NOTE 调用此函前需先排序
        """
        if len(nums) < n:
            return []

        ret = []
        if n == 2:
            return self.twoSum(nums, target=target)
        else:
            idx = 0
            while idx < len(nums):
                num = nums[idx]
                n_1_sum_ret = self.nSum(nums[idx + 1:], target=target-num, n=n-1)
                for r in n_1_sum_ret:
                    ret.append([num] + r)
                while idx < len(nums) and nums[idx] == num:
                    idx += 1
        return ret

# @lc code=end

