#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/merge-similar-items
from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        m = {}
        for v, w in items1 + items2:
            m[v] = m.get(v, 0) + w
        return list(sorted(m.items()))
