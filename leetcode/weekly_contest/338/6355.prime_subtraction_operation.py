#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/prime-subtraction-operation
from bisect import bisect_left
from typing import List


def prime_list(n):
    """质数列表(欧拉筛)."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        P = prime_list(n=1000)
        pre = 0
        for x in nums:
            if x <= pre:
                return False
            # 减去能减掉的最大质数
            idx = bisect_left(P, x - pre)
            pre = x - P[idx - 1] if idx != 0 else x
        return True
