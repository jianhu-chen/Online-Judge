#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-increasing-quadruplets
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        """
        1. 枚举中间的 j 和 k 效率更高
        2. 需要知道 k 右边有多少个数比 nums[j] 大, j 左边有多少个数比 nums[k] 小
        3. 预处理， 定义:
            great[k][x]: 在 k 右边且比 x 大的数的个数
            less[j][x]: 在 j 左边且比 x 小的数的个数
        """
        n = len(nums)
        great = [0] * n
        great[n - 1] = [0] * (n + 1)  # x 的范围: 1...n
        for k in reversed(range(2, n - 1)):  # k 的范围: 2...n-2
            great[k] = great[k + 1][:]  # deepcopy
            for x in range(nums[k + 1]):
                great[k][x] += 1

        ans = 0
        less = [0] * (n + 1)
        for j in range(1, n - 2):
            for x in range(nums[j - 1] + 1, n + 1):
                less[x] += 1
            # 枚举k
            for k in range(j + 1, n - 1):
                if nums[j] > nums[k]:
                    ans += less[nums[k]] * great[k][nums[j]]

        return ans
