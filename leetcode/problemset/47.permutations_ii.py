#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/permutations-ii
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def process(cur, rest):
            if not rest:
                return [cur]
            result = []
            visited = set()
            for idx in range(len(rest)):
                if rest[idx] in visited:
                    continue
                result += process([*cur, rest[idx]], rest[:idx] + rest[idx + 1:])
                visited.add(rest[idx])
            return result
        return process([], nums)
