#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/convert-an-array-into-a-2d-array-with-conditions
from typing import List
from collections import Counter


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        res = []
        while len(cnt):
            res.append([])
            remove = []
            for k in cnt:
                res[-1].append(k)
                cnt[k] -= 1
                if cnt[k] == 0:
                    remove.append(k)
            while remove:
                del cnt[remove.pop()]
        return res
