#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/3sum
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 参考有序数组的两数之和题目: https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted
        nums.sort()
        ans = set()
        for k in reversed(range(2, len(nums))):
            if k < len(nums) - 1 and nums[k] == nums[k + 1]:
                continue
            left, right = 0, k - 1
            while left < right:
                if nums[left] + nums[right] < -nums[k]:
                    left += 1
                elif nums[left] + nums[right] > -nums[k]:
                    right -= 1
                else:
                    ans.add((nums[left], nums[right], nums[k]))
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
        return list(ans)
