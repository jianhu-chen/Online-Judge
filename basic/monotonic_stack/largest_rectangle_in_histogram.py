#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import List


class LargestRectangleArea:
    """
    给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

    求在该柱状图中，能够勾勒出来的矩形的最大面积。

    ref: https://leetcode.cn/problems/largest-rectangle-in-histogram/
    """

    def solution1(self, heights: List[int]) -> int:
        """暴力解. O(N^2)"""
        n = len(heights)
        if not n:
            return 0

        ans = -float("inf")
        for L in range(n):
            for R in range(L, n):
                height = min(heights[L:R + 1])
                width = R - L + 1
                ans = max(ans, width * height)
        return ans

    def solution2(self, heights: List[int]) -> int:
        """单调递增栈. O(N)"""
        n = len(heights)
        if not n:
            return 0

        # left 存储严格小于当前值的左侧下标
        # right 存储严格小于当前值得右侧下标
        left, right = [0] * n, [n] * n

        stack: List[int] = []
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack: List[int] = []
        for i in range(n - 1, -1, -1):  # 从右往左遍历
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        return max(heights[i] * (right[i] - left[i] - 1) for i in range(n))

    def solution3(self, heights: List[int]) -> int:
        """单调递增栈. O(N)"""
        n = len(heights)
        if not n:
            return 0

        # left 存储严格小于当前值的左侧下标
        # right 存储小于等于当前值得右侧下标
        left, right = [0] * n, [n] * n
        stack: List[int] = []
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                top = stack.pop()
                right[top] = i
            # 准备入栈前记录i下标的左侧边界
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        return max(heights[i] * (right[i] - left[i] - 1) for i in range(n))


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = LargestRectangleArea()
        for _ in range(1000):
            heights = [
                random.randint(1, 10 ** 5)
                for _ in range(random.randint(1, 100))
            ]
            ans1 = obj.solution1(heights)
            ans2 = obj.solution2(heights)
            ans3 = obj.solution3(heights)
            self.assertEqual(ans1, ans2, (heights, ans1, ans2))
            self.assertEqual(ans1, ans3, (heights, ans1, ans3))


if __name__ == "__main__":
    obj = LargestRectangleArea()
    heights = [2, 1, 5, 6, 8]
    ans = obj.solution2(heights)
    print(ans)
    unittest.main()
