#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-the-number-of-good-subarrays
from typing import List
from collections import Counter


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        """双指针."""
        ans = 0
        left = 0
        good = 0
        cnt = Counter()
        for _, x in enumerate(nums):
            good += cnt[x]
            cnt[x] += 1
            ans += left  # 左端点可以在 left 左侧的任意位置
            while good >= k:
                ans += 1
                cnt[nums[left]] -= 1
                good -= cnt[nums[left]]
                left += 1
        return ans
