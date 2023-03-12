#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/subarray-sum-equals-k
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps = 0  # 前缀和
        cnt, ans = {0: 1}, 0
        for x in nums:
            ps += x
            ans += cnt.get(ps - k, 0)
            cnt[ps] = cnt.get(ps, 0) + 1
        return ans
