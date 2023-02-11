#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/first-bad-version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        ans = 0
        L, R = 1, n
        while L <= R:
            M = L + ((R - L) >> 1)
            if isBadVersion(M):
                ans = M
                R = M - 1
            else:
                L = M + 1
        return ans
