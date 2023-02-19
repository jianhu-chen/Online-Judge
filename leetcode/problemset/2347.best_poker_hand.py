#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/best-poker-hand
from typing import List
from collections import Counter


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        cnt = Counter(ranks)
        if max(cnt.values()) >= 3:
            return "Three of a Kind"
        if max(cnt.values()) >= 2:
            return "Pair"
        return "High Card"
