#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1
        while left <= right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]
