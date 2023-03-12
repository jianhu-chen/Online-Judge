#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/subarray-sums-divisible-by-k
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ps, cnt, ans = 0, {0: 1}, 0
        for x in nums:
            ps += x
            r = (ps + k) % k
            ans += cnt.get(r, 0)  # 数论: 同余定理
            cnt[r] = cnt.get(r, 0) + 1
        return ans
