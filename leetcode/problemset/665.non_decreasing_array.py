#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/non-decreasing-array
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n, cnt = len(nums), 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                cnt += 1
                if cnt > 1:
                    return False
                # case 1: [_7_, 5, 6]
                # case 2: [4, 4, _7_, 4, 6]
                # case 3: [4, 4, _7_, 5, 6]
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                # case 3: [5, 5, _7_, 4, 5, 6]
                else:
                    nums[i + 1] = nums[i]

        return True
