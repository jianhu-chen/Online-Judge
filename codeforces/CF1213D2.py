#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import heapq
from typing import List
from collections import defaultdict


class Solution:
    """https://codeforces.com/contest/1213/problem/D2."""

    def equalizingByDivision(self, nums: List[int], k: int) -> int:
        return self.solution2(nums, k)

    def solution1(self, nums: List[int], k: int) -> int:
        """O(UlogU), U = max(nums)"""
        cnt = defaultdict(list)
        mx = 0
        for x in nums:
            c = 0
            if x > mx:
                mx = x
            while x:
                if len(cnt[x]) < k:
                    heapq.heappush(cnt[x], -c)
                elif c < -cnt[x][0]:
                    heapq.heapreplace(cnt[x], -c)
                x >>= 1
                c += 1

        ans = float("inf")
        for x in range(1, mx + 1):
            if len(cnt[x]) != k:
                continue
            ans = min(ans, -sum(cnt[x]))
        return ans

    def solution2(self, nums: List[int], k: int) -> int:
        # 每一列表示有多少个数可以通过操作j次得到i
        mx = 200000
        a = [[] for _ in range(mx + 1)]
        for x in nums:
            a[x] = [1]

        ans = float("inf")
        for x in reversed(range(1, mx + 1)):
            if not a[x]:
                continue
            s, left = 0, k
            for j, c in enumerate(a[x]):
                if left <= c:
                    ans = min(ans, s + left * j)
                    break
                s += c * j
                left -= c

            x2 = x >> 1
            if not a[x2]:
                a[x2] = [0, *a[x]]
                continue
            for j, c in enumerate(a[x]):
                if j + 1 == len(a[x2]):
                    a[x2].extend(a[x][j:])
                    break
                a[x2][j + 1] += c
        return ans


if __name__ == "__main__":
    _, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(Solution().equalizingByDivision(nums, k))
