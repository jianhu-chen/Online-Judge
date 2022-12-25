#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List


class Islands:
    """给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

    岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

    此外，你可以假设该网格的四条边均被水包围。

    https://leetcode.cn/problems/number-of-islands
    """

    def solution1(self, grid: List[List[str]]) -> int:
        """遇1改为2."""
        M, N = len(grid), len(grid[0])

        def infect(x, y):
            if x < 0 or x > M - 1 or y < 0 or y > N - 1 or grid[x][y] != "1":
                return
            grid[x][y] = "2"
            infect(x - 1, y)
            infect(x + 1, y)
            infect(x, y - 1)
            infect(x, y + 1)

        result = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    result += 1
                    infect(i, j)
        return result
