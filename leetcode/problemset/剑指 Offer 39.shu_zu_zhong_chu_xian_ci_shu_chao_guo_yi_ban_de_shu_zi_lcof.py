#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n, cnt = len(nums), Counter()
        for x in nums:
            cnt[x] += 1
        for x, c in cnt.items():
            if c > n // 2:
                return x
