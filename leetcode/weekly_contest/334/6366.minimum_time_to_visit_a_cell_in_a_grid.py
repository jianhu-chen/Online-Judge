#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-time-to-visit-a-cell-in-a-grid
import heapq
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        """迪杰斯特拉算法."""
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        m, n = len(grid), len(grid[0])
        distance = [[float("inf")] * n for _ in range(m)]
        distance[0][0] = 0
        heap = [(0, (0, 0))]  # (dist, pos)
        while heap:
            dist, (x, y) = heapq.heappop(heap)
            # 截断
            if x == m - 1 and y == n - 1:
                return dist
            distance[x][y] = dist
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx == m or ny < 0 or ny == n:
                    continue
                new_dist = max(dist + 1, grid[nx][ny])
                # 反复来回跳, 根据奇偶性调整
                new_dist += 1 if not (new_dist - dist) & 1 else 0
                if new_dist < distance[nx][ny]:
                    distance[nx][ny] = dist
                    heapq.heappush(heap, (new_dist, (nx, ny)))
