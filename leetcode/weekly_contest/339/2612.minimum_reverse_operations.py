#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-reverse-operations
from bisect import bisect_left
from typing import List


class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        s = set(banned) | {p}
        not_banned = [[], []]
        for i in range(n):
            if i not in s:
                not_banned[i % 2].append(i)
        not_banned[0].append(n)
        not_banned[1].append(n)  # 哨兵

        fa = [list(range(len(not_banned[0]))), list(range(len(not_banned[1])))]

        def find(i: int, x: int) -> int:
            f = fa[i]
            if f[x] != x:
                f[x] = find(i, f[x])
            return f[x]

        def merge(i: int, from_: int, to: int) -> None:
            x, y = find(i, from_), find(i, to)
            fa[i][x] = y

        ans = [-1] * n
        q = [p]
        step = 0
        while q:
            tmp = q
            q = []
            for i in tmp:
                ans[i] = step
                # 从 mn 到 mx 的所有位置都可以翻转到
                mn = max(i - k + 1, k - i - 1)
                mx = min(i + k - 1, n * 2 - k - i - 1)
                a = not_banned[mn % 2]
                j = find(mn % 2, bisect_left(a, mn))
                while a[j] <= mx:
                    q.append(a[j])
                    merge(mn % 2, j, j + 1)  # 删除 j
                    j = find(mn % 2, j + 1)
            step += 1
        return ans
