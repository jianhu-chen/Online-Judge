#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-sorted-vowel-strings

class Solution:
    def countVowelStrings(self, n: int) -> int:
        def dfs(i: int, pre: str) -> int:
            if i == n:
                return 1
            return sum(dfs(i + 1, j) for j in range(pre, 5))

        return dfs(0, 0)
