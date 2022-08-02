#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import string
import unittest
from typing import List


def minus(s1: str, s2: str):
    count = dict()
    for c in s1:
        count[c] = count.get(c, 0) + 1
    for c in s2:
        count[c] = count.get(c, 0) - 1
    return "".join(c * count[c] for c in count if count[c] > 0)


class StickersToSpellWord:
    """
    给定一个字符串str, 给定一个字符串类型的数组arr, 出现的字符都是小写英文
    arr每一个字符串, 代表一张贴纸, 你可以把单个字符剪开使用, 目的是拼出str来
    返回需要至少多少张贴纸可以完成这个任务
    例子: str= "babac", arr = {"ba","c","abcd"}
    ba + ba + c  3  abcd + abcd 2  abcd+ba 2
    所以返回2

    ref: https://leetcode.com/problems/stickers-to-spell-word
    """

    def solution1(self, stickers: List[str], target: str) -> int:
        def process(stickers, target):
            if len(target) == 0:
                return 0
            ans = float("inf")
            for s in stickers:
                rest = minus(target, s)
                if len(rest) != len(target):
                    ans = min(ans, process(stickers, rest) + 1)
            return ans

        ans = process(stickers, target)
        return ans if ans != float("inf") else -1

    def solution2(self, stickers: List[str], target: str) -> int:
        def process(counts, rest):
            if len(rest) == 0:
                return 0

            rcounts = [0] * 26
            for c in rest:
                rcounts[ord(c) - ord('a')] += 1

            ans = float("inf")
            for idx in range(len(counts)):
                # 最关键的优化(重要的剪枝!这一步也是贪心!)
                if counts[idx][ord(rest[0]) - ord('a')] > 0:
                    rest_new = ""
                    for a in range(26):
                        nums = rcounts[a] - counts[idx][a]
                        if nums > 0:
                            rest_new += chr(a + ord('a')) * nums
                    ans = min(ans, process(counts, rest_new) + 1)
            return ans

        # [len(stickers), 26] 关键优化(用词频表替代贴纸数组)
        counts = [[0] * 26 for _ in range(len(stickers))]
        for i, s in enumerate(stickers):
            for c in s:
                counts[i][ord(c) - ord("a")] += 1
        ans = process(counts, target)
        return ans if ans != float("inf") else -1

    def solution3(self, stickers: List[str], target: str) -> int:
        """TODO (jianhu1): dp solution"""


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = StickersToSpellWord()
        s1_cost, s2_cost = 0, 0
        for _ in range(1000):
            target_length = random.randint(1, 20)
            target = "".join(random.choice(string.ascii_lowercase) for _ in range(target_length))
            num_stickers = random.randint(1, 5)
            sticker_length = random.randint(1, 5)
            stickers = [
                "".join(random.choice(string.ascii_lowercase) for _ in range(sticker_length))
                for _ in range(num_stickers)
            ]
            s = time.perf_counter()
            ans1 = obj.solution1(stickers, target)
            s1_cost += time.perf_counter() - s
            s = time.perf_counter()
            ans2 = obj.solution2(stickers, target)
            s2_cost += time.perf_counter() - s
            self.assertEqual(ans1, ans2)
        print(f"solution1 cost: {s1_cost}")
        print(f"solution2 cost: {s2_cost}")


if __name__ == "__main__":
    stickers = ["with", "example", "science"]
    target = "thehat"
    print(StickersToSpellWord().solution1(stickers, target))
    print(StickersToSpellWord().solution2(stickers, target))
    unittest.main()
