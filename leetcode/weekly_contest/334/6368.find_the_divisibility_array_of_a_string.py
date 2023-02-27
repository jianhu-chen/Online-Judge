#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-the-divisibility-array-of-a-string
from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        nums = list(map(int, word))
        s, ans = 0, []
        for x in nums:
            s = (s * 10 + x) % m
            ans.append(0 if s else 1)
        return ans
