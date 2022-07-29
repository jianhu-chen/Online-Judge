#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest

import numpy as np


class BobDie:
    """
    给定5个参数，N，M，row，col，k
    表示在N*M的区域上，醉汉Bob初始在(row,col)位置
    Bob一共要迈出k步，且每步都会等概率向上下左右四个方向走一个单位
    任何时候Bob只要离开N*M的区域，就直接死亡
    返回k步之后，Bob还在N*M的区域的概率
    """

    def solution1(self, N, M, row, col, k):
        def process(N, M, row, col, k):
            if row < 0 or row > N - 1 or col < 0 or col > M - 1:
                return 0
            if k == 0:
                return 1
            a1 = process(N, M, row - 1, col, k - 1)
            a2 = process(N, M, row + 1, col, k - 1)
            a3 = process(N, M, row, col - 1, k - 1)
            a4 = process(N, M, row, col + 1, k - 1)
            return a1 + a2 + a3 + a4
        num_lives = process(N, M, row, col, k)
        return num_lives / 4 ** k

    def solution2(self, N, M, row, col, k):
        def get_value(dp, h, x, y):
            if x < 0 or x > N - 1 or y < 0 or y > M - 1:
                return 0
            return dp[h, x, y]
        dp = np.zeros(shape=[k + 1, N, M], dtype=np.int32)
        dp[0] = 1
        for i in range(1, k + 1):
            for r in range(N):
                for c in range(M):
                    a1 = get_value(dp, i - 1, r - 1, c)
                    a2 = get_value(dp, i - 1, r + 1, c)
                    a3 = get_value(dp, i - 1, r, c - 1)
                    a4 = get_value(dp, i - 1, r, c + 1)
                    dp[i, r, c] = a1 + a2 + a3 + a4
        return dp[k, row, col] / 4 ** k


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = BobDie()
        for _ in range(100):
            N = random.randint(1, 15)
            M = random.randint(1, 15)
            row = random.randint(0, N - 1)
            col = random.randint(0, M - 1)
            k = random.randint(0, 10)
            ans1 = obj.solution1(N, M, row, col, k)
            ans2 = obj.solution2(N, M, row, col, k)
            self.assertEqual(ans1, ans2)


if __name__ == "__main__":
    unittest.main()
