# -*- coding: utf-8 -*-
from typing import List


class Solution:

    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        while len(nums) > 1:
            for i in range(0, len(nums) // 2):
                slice = nums[2 * i: 2 * i + 2]
                nums[i] = max(slice) if i % 2 else min(slice)
            nums = nums[:len(nums) // 2]
        return nums[0]
