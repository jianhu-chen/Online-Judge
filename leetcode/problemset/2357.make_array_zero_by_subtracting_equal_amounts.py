#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/make-array-zero-by-subtracting-equal-amounts
from typing import List
from collections import Counter


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return len(cnt) - 1 if cnt[0] else len(cnt)
