#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import List


class MaxSlidingWindow:
    """
    给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
    你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

    返回 滑动窗口中的最大值 。

    ref: https://leetcode.cn/problems/sliding-window-maximum
    """

    def solution1(self, nums: List[int], k: int) -> List[int]:
        """暴力解."""
        ans = []
        for end in range(k, len(nums) + 1):
            ans.append(max(nums[end - k:end]))
        return ans

    def solution2(self, nums: List[int], k: int) -> List[int]:
        """滑动窗口."""
        ans = []
        # 双向队列 保存当前窗口最大值的数组位置 保证队列中数组位置的数值按从大到小排序
        deque = []
        for i in range(len(nums)):
            # 向队列中加入当前下标 (可能需要弹出队列尾部的过期值)
            while deque and nums[deque[-1]] <= nums[i]:
                deque.pop()
            deque.append(i)
            # 保持双端队列中的小标在窗口内, 过期的就移除掉
            if deque[0] == i - k:
                deque.pop(0)
            # 窗口形成了之后, 每往后移动一格就要生成一个窗口最大值
            if i >= k - 1:
                ans.append(nums[deque[0]])
        return ans


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = MaxSlidingWindow()
        for _ in range(500):
            nums = [
                random.randint(-10000, 10000)
                for _ in range(1, 10 ** 3)
            ]
            k = random.randint(1, len(nums))
            ans1 = obj.solution1(nums, k)
            ans2 = obj.solution2(nums, k)
            self.assertEqual(ans1, ans2, (nums, k, ans1, ans2))


if __name__ == "__main__":
    unittest.main()
