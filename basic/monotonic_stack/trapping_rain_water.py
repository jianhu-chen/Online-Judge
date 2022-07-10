#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import List


class Trap:
    """
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png)

    上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。

    ref: https://leetcode.cn/problems/trapping-rain-water/
    """

    def solution1(self, height: List[int]) -> int:
        """暴力解. O(N^2)"""
        ans = 0
        for i in range(len(height)):
            # 找左右两边柱子的最大值, 取其中较小者减去当前柱子的高度
            L = max(height[:i + 1])
            R = max(height[i:])
            ans += min(L, R) - height[i]
        return ans

    def solution2(self, height: List[int]) -> int:
        """单调递减栈. O(N)"""
        ans = 0
        stack: List[int] = []
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                if stack:
                    w = i - stack[-1] - 1
                    h = min(height[stack[-1]], height[i]) - height[top]
                    ans += w * h
            stack.append(i)
        return ans

    def solution3(self, height: List[int]) -> int:
        """动态规划. O(N)"""
        left_max = [0] * len(height)
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max = [0] * len(height)
        right_max[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        ans = 0
        for i in range(len(height)):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = Trap()
        for _ in range(1000):
            height = [
                random.randint(1, 10 ** 5)
                for _ in range(random.randint(1, 500))
            ]
            ans1 = obj.solution1(height)
            ans2 = obj.solution2(height)
            ans3 = obj.solution3(height)
            self.assertEqual(ans1, ans2, (height, ans1, ans2))
            self.assertEqual(ans1, ans3, (height, ans1, ans3))


if __name__ == "__main__":
    obj = Trap()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    ans = obj.solution1(height)
    print(ans)
    height = [4, 2, 0, 3, 2, 5]
    ans = obj.solution1(height)
    print(ans)
    unittest.main()
