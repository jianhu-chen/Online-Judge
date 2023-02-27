#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/swim-in-rising-water
import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = ((-1, 0), (0, -1), (1, 0), (0, 1))
        distance = [[float("inf")] * n for _ in range(m)]
        heap = [[grid[0][0], (0, 0)]]
        while heap:
            dist, (x, y) = heapq.heappop(heap)
            if x == m - 1 and y == n - 1:
                return dist
            distance[x][y] = dist
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx == m or ny < 0 or ny == n:
                    continue
                new_dist = max(dist, grid[nx][ny])
                if new_dist < distance[nx][ny]:
                    distance[nx][ny] = new_dist
                    heapq.heappush(heap, (new_dist, (nx, ny)))
