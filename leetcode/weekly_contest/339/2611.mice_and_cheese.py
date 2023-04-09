#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/mice-and-cheese
from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        reward = sorted(zip(reward1, reward2), key=lambda x: x[1] - x[0])
        return sum(reward[i][0] if i < k else reward[i][1] for i in range(len(reward)))
