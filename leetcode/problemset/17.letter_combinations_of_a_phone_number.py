#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapper = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)

        ans = []
        path = [""] * n

        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return
            for c in mapper[int(digits[i])]:
                path[i] = c
                dfs(i + 1)

        dfs(0)
        return ans if n != 0 else []
