#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/row-with-maximum-ones
from typing import List
from collections import Counter


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        tmp = [Counter(m) for m in mat]
        ids = sorted(range(len(tmp)), key=lambda i: -tmp[i][1])
        return [ids[0], tmp[ids[0]][1]]
