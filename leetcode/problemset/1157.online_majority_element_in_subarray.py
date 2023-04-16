#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/online-majority-element-in-subarray
from bisect import bisect_left, bisect_right
from random import randint
from typing import List
from collections import defaultdict


class MajorityChecker:
    K = 10

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.loc = defaultdict(list)
        for i, x in enumerate(arr):
            self.loc[x].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(self.K):
            x = randint(left, right)
            index = self.loc[self.arr[x]]
            cnt = bisect_right(index, right) - bisect_left(index, left)
            if cnt >= threshold:
                return self.arr[x]
            elif cnt * 2 >= right - left + 1:
                return -1
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
