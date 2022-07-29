#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import unittest
from typing import List

import numpy as np


class MinimumPathSum:
    """
    给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

    说明：每次只能向下或者向右移动一步。

    https://leetcode.cn/problems/minimum-path-sum
    """

    def solution1(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def process(grid, x, y, path_sum):
            if x == m - 1 and y == n - 1:
                return path_sum
            ans = float("inf")
            if x != m - 1:
                ans = min(ans, process(grid, x + 1, y, path_sum + grid[x + 1][y]))
            if y != n - 1:
                ans = min(ans, process(grid, x, y + 1, path_sum + grid[x][y + 1]))
            return ans
        return process(grid, 0, 0, grid[0][0])

    def solution2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = np.zeros(shape=(m + 1, n + 1))
        dp[:, -1] = np.inf
        dp[-1, :] = np.inf
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    dp[i][j] = grid[i][j]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j]
        return int(dp[0][0])


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = MinimumPathSum()
        s1_cost, s2_cost = 0, 0
        for _ in range(1000):
            m = random.randint(2, 10)
            n = random.randint(2, 10)
            grid = [
                [random.randint(0, 10) for _ in range(m)]
                for _ in range(n)
            ]
            s = time.perf_counter()
            ans1 = obj.solution1(grid)
            s1_cost += time.perf_counter() - s
            s = time.perf_counter()
            ans2 = obj.solution2(grid)
            s2_cost += time.perf_counter() - s
            self.assertEqual(ans1, ans2)
        print("solution1 cost:", s1_cost)
        print("solution2 cost:", s2_cost)


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(MinimumPathSum().solution1(grid))
    print(MinimumPathSum().solution2(grid))
    unittest.main()
