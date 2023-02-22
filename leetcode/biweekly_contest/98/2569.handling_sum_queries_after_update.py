#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/handling-sum-queries-after-update
from typing import List


class LazySegmentTree:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.ones = [0] * (4 * self.n)
        self.lazy = [False] * (4 * self.n)
        self._build(0, 0, self.n - 1)

    def _build(self, o: int, ll: int, rr: int) -> None:
        if ll == rr:
            self.ones[o] = self.nums[ll]
            return
        left, right = 2 * o + 1, 2 * o + 2
        mid = (ll + rr) // 2
        self._build(left, ll, mid)
        self._build(right, mid + 1, rr)
        self.ones[o] = self.ones[left] + self.ones[right]

    def _do(self, o: int, ll: int, rr: int) -> None:
        self.ones[o] = rr - ll + 1 - self.ones[o]
        self.lazy[o] = not self.lazy[o]

    def _pushdown(self, o: int, ll: int, rr: int) -> None:
        if self.lazy[o]:
            left, right = 2 * o + 1, 2 * o + 2
            mid = (ll + rr) // 2
            self._do(left, ll, mid)
            self._do(right, mid + 1, rr)
            self.lazy[o] = False

    def _update(self, o: int, ll: int, rr: int, ql: int, qr: int) -> None:
        if ql <= ll and rr <= qr:
            self._do(o, ll, rr)
            return
        self._pushdown(o, ll, rr)
        left, right = 2 * o + 1, 2 * o + 2
        mid = (ll + rr) // 2
        if ql <= mid:
            self._update(left, ll, mid, ql, qr)
        if mid + 1 <= qr:
            self._update(right, mid + 1, rr, ql, qr)
        self.ones[o] = self.ones[left] + self.ones[right]

    def _query(self, o: int, ll: int, rr: int, ql: int, qr: int) -> int:
        if ql <= ll and rr <= qr:
            return self.ones[o]
        left, right = 2 * o + 1, 2 * o + 2
        mid = (ll + rr) // 2
        self._pushdown(o, ll, rr)
        ans = 0
        if ql <= mid:
            ans += self._query(left, ll, mid, ql, qr)
        if mid + 1 <= qr:
            ans += self._query(right, mid + 1, rr, ql, qr)
        return ans

    def update(self, ql: int, qr: int) -> None:
        self._update(0, 0, self.n - 1, ql, qr)

    def query(self, ql: int, qr: int) -> int:
        return self._query(0, 0, self.n - 1, ql, qr)


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        """Lazy 线段树."""
        t = LazySegmentTree(nums1)
        s = sum(nums2)
        ans = []
        for q, l, r in queries:
            if q == 1:
                t.update(l, r)
            elif q == 2:
                s += l * t.query(0, len(nums1) - 1)
            else:
                ans.append(s)
        return ans
