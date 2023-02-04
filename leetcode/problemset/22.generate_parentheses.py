#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/generate-parentheses
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, path = [], []

        def dfs(i, lrest, rrest, cnt):
            if cnt < 0:  # 非法括号剪枝
                return
            if i == 2 * n:
                ans.append("".join(path))
                return
            # 选左
            if lrest > 0:
                path.append("(")
                dfs(i + 1, lrest - 1, rrest, cnt + 1)
                path.pop()
            # 选右
            if rrest > 0:
                path.append(")")
                dfs(i + 1, lrest, rrest - 1, cnt - 1)
                path.pop()

        dfs(0, n, n, 0)
        return ans
