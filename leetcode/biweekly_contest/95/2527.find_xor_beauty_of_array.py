#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-xor-beauty-of-array
from typing import List
from functools import reduce


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        return self.solution2(nums)

    def solution1(self, nums: List[int]) -> int:
        """暴力解."""
        n, ans = len(nums), 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    ans ^= (nums[i] | nums[j]) & nums[k]
        return ans

    def solution2(self, nums: List[int]) -> int:
        # 推导见: https://tinyurl.com/486a58hw
        return reduce(lambda x, y: x ^ y, nums)
