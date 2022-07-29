#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import string
import unittest
from typing import List
from collections import Counter


class String:

    def __init__(self, s=""):
        self.s = s

    def __sub__(self, other):
        c1 = Counter(self.s)
        c2 = Counter(other.s)
        c1.subtract(c2)
        ans = ""
        for k, v in c1.items():
            if v > 0:
                ans += k * v
        return String(ans)

    def __len__(self):
        return len(self.s)

    def __repr__(self) -> str:
        return str(self.s)


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
                rest = target - s
                if len(rest) != len(target):
                    ans = min(ans, process(stickers, rest) + 1)
            return ans

        stickers = [String(x) for x in stickers]
        target = String(target)
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
                if counts[idx][ord(target[0]) - ord('a')] > 0:
                    rest_new = ""
                    for a in range(26):
                        if rcounts[a] > 0:
                            rest_new += (rcounts[a] - counts[idx][a]) * chr(a + ord('a'))
                    ans = min(ans, process(counts, rest_new))
            return ans

        # [len(stickers), 26] 关键优化(用词频表替代贴纸数组)
        counts = [[0] * 26 for _ in range(len(stickers))]
        for i, s in enumerate(stickers):
            for c in s:
                counts[i][ord(c) - ord("a")] += 1
        ans = process(counts, target)
        return ans if ans != float("inf") else -1

    def solution3(self, stickers: List[str], target: str) -> int:
        pass


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = StickersToSpellWord()
        s1_cost, s2_cost, s3_cost = 0, 0, 0
        for _ in range(10):
            target_length = random.randint(1, 100)
            target = "".join(random.choice(string.ascii_lowercase) for _ in range(target_length))
            num_stickers = random.randint(1, 10)
            sticker_length = random.randint(1, 10)
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
            s = time.perf_counter()
            ans3 = obj.solution3(stickers, target)
            s3_cost += time.perf_counter() - s
            self.assertEqual(ans1, ans2)
            self.assertEqual(ans1, ans3)
        print(f"solution1 cost: {s1_cost}")
        print(f"solution2 cost: {s2_cost}")
        print(f"solution3 cost: {s3_cost}")


if __name__ == "__main__":
    stickers = ["with", "example", "science"]
    target = "thehat"
    print(StickersToSpellWord().solution1(stickers, target))
    print(StickersToSpellWord().solution2(stickers, target))
    # unittest.main()
