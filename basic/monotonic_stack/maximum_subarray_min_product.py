#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import List


class MaxSumMinProduct:
    """
    一个数组的 最小乘积 定义为这个数组中 最小值 乘以 数组的 和 。

    比方说，数组 [3,2,5] （最小值是 2）的最小乘积为 2 * (3+2+5) = 2 * 10 = 20 。
    给你一个正整数数组 nums ，请你返回 nums 任意 非空子数组 的最小乘积 的 最大值 。
    由于答案可能很大，请你返回答案对  109 + 7 取余 的结果。

    请注意，最小乘积的最大值考虑的是取余操作 之前 的结果。
    题目保证最小乘积的最大值在 不取余 的情况下可以用 64 位有符号整数 保存。

    子数组 定义为一个数组的 连续 部分。

    ref: https://leetcode.cn/problems/maximum-subarray-min-product
    """

    def solution1(self, nums: List[int]) -> int:
        """暴力解. O(N^2)"""
        ans = -float("inf")
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                ans = max(ans, min(nums[i:j]) * sum(nums[i:j]))
        return ans % ((10 ** 9) + 7)

    def solution2(self, nums: List[int]) -> int:
        """
        单调递增栈. O(N).

        思路: 依次遍历所有下标 i, 找到以下标 i 为最小值的最长子数组, 更新最小乘积.
        即: 从 i 往两边扩, 两边分别找到第一个比 nums[i] 小的数.
        """
        n = len(nums)
        if not n:
            return 0

        presum = []
        for num in nums:
            presum.append(presum[-1] + num if presum else num)
        presum += [0]  # !NOTE: 哨兵, 无左边界情况取-1下标

        left, right = [0] * n, [n] * n

        stack: List[int] = []
        for i in range(n):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack: List[int] = []
        for i in range(n - 1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        ans = max(nums[i] * (presum[right[i] - 1] - presum[left[i]]) for i in range(n))
        return ans % ((10 ** 9) + 7)

    def solution3(self, nums: List[int]) -> int:
        """
        单调递增栈. O(N).

        与solution2解法一样, 但右侧边界非严格小于弹出元素 (而是小于等于, 由于左边界严格, 所以最终答案也正确).
        """
        n = len(nums)
        if not n:
            return 0

        # 前缀和
        presum = []
        for num in nums:
            presum.append(presum[-1] + num if presum else num)
        presum.append(0)  # 哨兵

        stack: List[int] = []
        left, right = [0] * n, [n] * n
        for i in range(n):
            while stack and nums[i] <= nums[stack[-1]]:
                top = stack.pop()
                right[top] = i  # 非严格, 右侧第一个小于或等于 nums[top] 的元素下标
            left[i] = stack[-1] if stack else -1  # 严格, 左侧第一个小于 nums[top] 的元素下标
            stack.append(i)

        ans = max(nums[i] * (presum[right[i] - 1] - presum[left[i]]) for i in range(n))
        return ans % ((10 ** 9) + 7)


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = MaxSumMinProduct()
        for _ in range(1000):
            nums = [
                random.randint(0, 10 ** 7)
                for _ in range(random.randint(1, 100))
            ]
            ans1 = obj.solution1(nums)
            ans2 = obj.solution2(nums)
            ans3 = obj.solution3(nums)
            self.assertEqual(ans1, ans2, (nums, ans1, ans2))
            self.assertEqual(ans1, ans3, (nums, ans1, ans3))


if __name__ == "__main__":
    nums = [1, 2, 3, 2]
    obj = MaxSumMinProduct()
    ans1 = obj.solution1(nums)
    print(ans1)
    ans2 = obj.solution2(nums)
    print(ans2)
    ans3 = obj.solution3(nums)
    print(ans3)
    unittest.main()
