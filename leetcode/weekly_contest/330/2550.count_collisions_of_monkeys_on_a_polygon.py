#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-collisions-of-monkeys-on-a-polygon

class Solution:
    def monkeyMove(self, n: int) -> int:
        # 正难则反, 只有全部顺时针和全部逆时针才不会碰撞, 因此答案为 2 **n - 2
        MOD = 10 ** 9 + 7
        return (pow(2, n, MOD) - 2) % MOD
