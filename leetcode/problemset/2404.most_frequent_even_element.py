#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/most-frequent-even-element
from typing import List
from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        tmp = sorted(filter(lambda x: not x[0] & 1, Counter(nums).items()), key=lambda x: [-x[1], x[0]])
        return tmp[0][0] if tmp else -1
