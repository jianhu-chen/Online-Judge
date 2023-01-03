#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/distinct-prime-factors-of-product-of-array
from typing import List


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            # 对每个数分解质因数
            i = 2
            while i * i <= n:
                if n % i == 0:
                    s.add(i)
                    n //= i
                else:
                    i += 1
            if n > 1:
                s.add(n)
        return len(s)
