#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/closest-prime-numbers-in-range
from typing import List

# 参考: https://leetcode.cn/problems/closest-prime-numbers-in-range/solution/yu-chu-li-zhi-shu-mei-ju-by-endlesscheng-uw2b/


def all_prime1(M) -> list:
    """埃式筛.

    遍历到数i时, 筛掉range(i*i, right, i)中的数.
    """
    is_prime = [True] * (M + 1)
    primes = []
    for i in range(2, M + 1):
        if not is_prime[i]:
            continue
        primes.append(i)
        for j in range(i * i, M + 1, i):
            is_prime[j] = False
    return primes


def all_prime2(M) -> list:
    """线性筛(欧拉筛), 每个合数只被标记一次.

    遍历到数i时, 筛掉primes[j]*i的数。另外, 线性筛的核心在于用最小的素因子筛掉合数, 所以当遍历到i % primes[j] ==
    0i时就需要退出循环 因为i乘上primes[j]后面的质数的结果一定会被primes[j]的倍数筛掉, 就不需要在i这里先筛一次。举个例子,
    12应该被2*6(i=6)筛掉, 而不是被3*4(i=4)筛掉.
    """
    is_prime = [True] * (M + 1)
    primes = []
    for i in range(2, M + 1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if p * i > M:
                break
            is_prime[p * i] = False
            if i % p == 0:
                break
    return primes


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = all_prime1(10 ** 6)

        # 二分查找找出第一个大于等于left的质数
        L, R = 0, len(primes) - 1
        start = -1
        while L <= R:
            M = L + ((R - L) >> 1)
            if primes[M] >= left:
                start = M
                R = M - 1
            else:
                L = M + 1

        if start == -1:
            return -1, -1

        p = q = -1
        for idx in range(start + 1, len(primes)):
            if primes[idx] > right:
                break
            if p == -1 or primes[idx] - primes[idx - 1] < q - p:
                p = primes[idx - 1]
                q = primes[idx]

        return p, q
