#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/two-sum
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}  # num to idx
        for idx, n in enumerate(nums):
            rest = target - n
            if rest in visited:
                return visited[rest], idx
            visited[n] = idx
