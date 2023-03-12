#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-the-number-of-beautiful-subarrays
from typing import List
from itertools import accumulate


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        ps = list(accumulate(nums, int.__xor__, initial=0))
        cnt, ans = {}, 0
        for x in ps:
            ans += cnt.get(x, 0)
            cnt[x] = cnt.get(x, 0) + 1
        return ans
