#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = [0] * 32
        for x in nums:
            for i in range(32):
                cnt[i] += x & 1
                x >>= 1

        n, ans = 1, 0
        for i in range(32):
            if cnt[i] % 3:
                ans += n
            n *= 2
        return ans
