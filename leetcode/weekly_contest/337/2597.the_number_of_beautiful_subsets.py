#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/the-number-of-beautiful-subsets
from typing import List
from collections import Counter


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans, n = 0, len(nums)
        cnt = Counter()

        def dfs(i, pre):
            if cnt and pre == i - 1:
                nonlocal ans
                ans += 1
            if i == n:
                return
            # 可以选?
            if not cnt[nums[i] + k] and not cnt[nums[i] - k]:
                cnt[nums[i]] += 1
                dfs(i + 1, i)
                cnt[nums[i]] -= 1
            # 不选
            dfs(i + 1, pre)

        dfs(0, -1)
        return ans
