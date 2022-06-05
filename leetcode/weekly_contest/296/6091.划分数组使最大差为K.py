# -*- coding: utf-8 -*-
from typing import List


class Solution:

    def partitionArray(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(set(nums))

        nums.sort()
        cnt = 0
        start = 0
        while start < len(nums):
            start = start + self.find_right_index(nums[start:], k) + 1
            cnt += 1
        return cnt

    def find_right_index(self, nums, k):
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] - nums[0] <= k:
                return idx
