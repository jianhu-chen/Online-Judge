#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import string
import unittest
from typing import Any, List
from functools import reduce
from itertools import permutations


def quick_sort(arr: List[Any], compare: callable) -> None:
    def _quick_sort(arr: List[Any], L: int, R: int) -> None:
        if L >= R:
            return

        # random pivot
        pivot_idx = random.randint(L, R)
        arr[pivot_idx], arr[R] = arr[R], arr[pivot_idx]
        # partition
        pivot = arr[R]
        left, right = L - 1, R
        idx = L
        while idx < right:
            cmp = compare(arr[idx], pivot)
            if cmp > 0:
                right -= 1
                arr[right], arr[idx] = arr[idx], arr[right]
            elif cmp < 0:
                left += 1
                arr[left], arr[idx] = arr[idx], arr[left]
                idx += 1
            else:
                idx += 1
        # move pivot to correct position
        arr[right], arr[R] = arr[R], arr[right]
        # recursively sort
        _quick_sort(arr, L, left)
        _quick_sort(arr, right + 1, R)
    _quick_sort(arr, 0, len(arr) - 1)


class LowestLexicography:

    def solution1(self, strs: List[str]) -> str:
        candidates = ["".join(x) for x in permutations(strs)]
        return reduce(lambda a, b: a if a < b else b, candidates)

    def solution2(self, strs: List[str]) -> str:
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return 1
            elif a + b < b + a:
                return -1
            else:
                return 0
        quick_sort(strs, compare=compare)
        return "".join(strs)


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = LowestLexicography()
        for _ in range(100):
            strs = [
                "".join(random.choices(string.ascii_lowercase, k=random.randint(1, 5)))
                for _ in range(random.randint(1, 10))
            ]
            ans1 = obj.solution1(strs[:])
            ans2 = obj.solution2(strs[:])
            self.assertEqual(ans1, ans2)


if __name__ == "__main__":
    unittest.main()
