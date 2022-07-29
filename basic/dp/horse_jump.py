#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest

import numpy as np


class HorseJump:
    """
    请同学们自行搜索或者想象一个象棋的棋盘，
    然后把整个棋盘放入第一象限，棋盘的最左下角是(0,0)位置
    那么整个棋盘就是横坐标上9条线、纵坐标上10条线的区域
    给你三个 参数 x，y，k
    返回“马”从(0,0)位置出发，必须走k步
    最后落在(x,y)上的方法数有多少种?
    """

    def solution1(self, x, y, k):
        def process(x, y, k):
            if x < 0 or x > 9 or y < 0 or y > 8:
                return 0
            if k == 0:
                return 1 if x == 0 and y == 0 else 0
            a1 = process(x - 2, y + 1, k - 1)
            a2 = process(x - 1, y + 2, k - 1)
            a3 = process(x + 1, y + 2, k - 1)
            a4 = process(x + 2, y + 1, k - 1)
            a5 = process(x - 2, y - 1, k - 1)
            a6 = process(x - 1, y - 2, k - 1)
            a7 = process(x + 1, y - 2, k - 1)
            a8 = process(x + 2, y - 1, k - 1)
            return a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
        return process(x, y, k)

    def solution2(self, x, y, k):
        def get_value(dp, h, x, y):
            """Return the value if the position is in the dp"""
            if h < 0 or x < 0 or x > 9 or y < 0 or y > 8:
                return 0
            return dp[h][x][y]

        dp = np.zeros(shape=[k + 1, 10, 9], dtype=int)
        dp[0][0][0] = 1
        for h in range(1, k + 1):
            for col in range(10):
                for row in range(9):
                    a1 = get_value(dp, h - 1, col - 2, row + 1)
                    a2 = get_value(dp, h - 1, col - 1, row + 2)
                    a3 = get_value(dp, h - 1, col + 1, row + 2)
                    a4 = get_value(dp, h - 1, col + 2, row + 1)
                    a5 = get_value(dp, h - 1, col - 2, row - 1)
                    a6 = get_value(dp, h - 1, col - 1, row - 2)
                    a7 = get_value(dp, h - 1, col + 1, row - 2)
                    a8 = get_value(dp, h - 1, col + 2, row - 1)
                    dp[h][col][row] = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
        return dp[k][x][y]


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = HorseJump()
        for _ in range(100):
            x = random.randint(0, 9)
            y = random.randint(0, 8)
            k = random.randint(1, 7)
            ans1 = obj.solution1(x, y, k)
            ans2 = obj.solution2(x, y, k)
            self.assertEqual(ans1, ans2)


if __name__ == "__main__":
    unittest.main()
