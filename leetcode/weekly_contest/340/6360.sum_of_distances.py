#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/sum-of-distances
from typing import List
from collections import Counter


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # 左到右
        m, cnt = {}, Counter()
        left = [0 for _ in range(len(nums))]
        for i, x in enumerate(nums):
            if x in m:
                left[i] += left[m[x]] + (i - m[x]) * cnt[x]
            m[x] = i
            cnt[x] += 1

        # 右到左
        m, cnt = {}, Counter()
        right = [0 for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            x = nums[i]
            if x in m:
                right[i] += right[m[x]] + (m[x] - i) * cnt[x]
            m[x] = i
            cnt[x] += 1
        return [x + y for x, y in zip(left, right)]
