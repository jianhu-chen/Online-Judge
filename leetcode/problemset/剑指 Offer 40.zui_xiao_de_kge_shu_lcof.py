#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)

        def qs(L, R, rest):
            if L >= R:
                return
            left = L - 1
            idx = L
            while idx < R:
                if arr[idx] < arr[R]:
                    left += 1
                    arr[left], arr[idx] = arr[idx], arr[left]
                idx += 1
            left += 1
            arr[left], arr[R] = arr[R], arr[left]
            # special
            if left - L + 1 == rest:
                return
            elif left - L + 1 < rest:
                qs(left + 1, R, rest - (left - L + 1))
            else:
                qs(L, left - 1, rest)

        qs(0, n - 1, k)
        return arr[:k]
