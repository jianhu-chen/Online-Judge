#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/lexicographically-smallest-string-after-applying-operations
from collections import deque


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ans = s
        visited = set()
        q = deque([s])
        while q:
            s = q.popleft()
            if s < ans:
                ans = s
            n1 = s[-b:] + s[:-b]
            n2 = "".join(
                str((int(ch) + a) % 10) if i & 1 else ch
                for i, ch in enumerate(s)
            )
            for nxt in (n1, n2):
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
        return ans
