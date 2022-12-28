#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimize-the-maximum-of-two-arrays
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)


def LCM(a, b):
    return a * b / GCD(a, b)


class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        # d1 = 4, d2 = 6
        # arr1: 1 2 3   5 6 7   9 10 11   13 ...
        # arr2: 1 2 3 4 5   7 8 9 10 11   13 ...
        # 假设答案是x, 那么:
        # arr1独占: 是 d2 的倍数 且 不是 d1 的倍数(且不是lcm的倍数) => x // d2 - x // lcm 个, 记为 x1
        # arr2独占: 是 d1 的倍数 且 不是 d2 的倍数(且不是lcm的倍数) => x // d1 - x // lcm 个, 记为 x2
        # 共享的: 不是 d1 的倍数, 也不是 d2 的倍数: 共 x - (x // d1 + x // d2 - x // lcm) 个, 记为common
        # 因此, 只需要找到满足  common >= (uniqueCnt1 - x1) + (uniqueCnt2 - x2) 的 最小 x 即可
        # 最坏情况下, d1, d2 = 2, 此时x的结果为 2 * (uniqueCnt1 + uniqueCnt2)
        L, R = 1, 2 * (uniqueCnt1 + uniqueCnt2)
        lcm = LCM(divisor1, divisor2)
        ans = 0
        while L <= R:
            M = L + ((R - L) >> 1)
            x1 = M // divisor2 - M // lcm
            x2 = M // divisor1 - M // lcm
            common = M - (M // divisor1 + M // divisor2 - M // lcm)
            if common >= max(uniqueCnt1 - x1, 0) + max(uniqueCnt2 - x2, 0):
                R = M - 1
                ans = M
            else:
                L = M + 1
        return ans
