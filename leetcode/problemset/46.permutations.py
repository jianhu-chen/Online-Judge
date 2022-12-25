#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def process(cur, rest):
            if not rest:
                return [cur]

            result = []
            for i in range(len(rest)):
                result += process([*cur, rest[i]], rest[:i] + rest[i + 1:])
            return result

        return process([], nums)
