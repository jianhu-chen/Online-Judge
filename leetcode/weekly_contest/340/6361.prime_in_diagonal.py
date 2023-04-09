#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/prime-in-diagonal
from typing import List


def is_prime(n):
    """判断是否为质数."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n, res = len(nums), 0
        for i in range(n):
            if is_prime(nums[i][i]) and nums[i][i] > res:
                res = nums[i][i]
            if is_prime(nums[i][n - i - 1]) and nums[i][n - i - 1] > res:
                res = nums[i][n - i - 1]
        return res
