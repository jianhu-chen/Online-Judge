#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/separate-the-digits-in-an-array
from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            tmp = []
            while x:
                tmp.append(x % 10)
                x //= 10
            ans.extend(tmp[::-1])
        return ans
