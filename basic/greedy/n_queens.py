#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from typing import List


class NQueues:
    """
    按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

    n皇后问题 研究的是如何将n个皇后放置在 n x n 的棋盘上，并且使皇后彼此之间不能相互攻击。

    给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

    每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

    https://leetcode.cn/problems/n-queens/
    """

    def solution1(self, n: int) -> List[List[str]]:
        """O(N!)"""

        def is_valid(lines: List[int], col_idx: int):
            """在lines棋局的基础上, 下一行放置在 col_idx 位置是否有效."""
            row_idx = len(lines)
            for pre_row_idx, pre_col_idx in enumerate(lines):
                row_faild = row_idx == pre_row_idx
                col_faild = col_idx == pre_col_idx
                x_faild = abs(col_idx - pre_col_idx) == abs(row_idx - pre_row_idx)
                if row_faild or col_faild or x_faild:
                    return False
            return True

        def process(i: int, n: int, lines: List[int]):
            if i == n:
                return [lines]

            ans = []
            for j in range(n):
                if is_valid(lines, j):
                    ans += process(i + 1, n, [*lines, j])
            return ans

        ans = process(0, n, [])
        result = [["" for _ in range(n)] for _ in range(len(ans))]
        for i, s in enumerate(ans):
            for row, col in enumerate(s):
                line = ["."] * n
                line[col] = "Q"
                result[i][row] = "".join(line)

        return result

    def solution2(self, n: int) -> List[List[str]]:
        """位运算优化."""
        if n > 32 or n < 1:
            return []

        def process(
            limit: int,
            col_limit: int,
            left_limit: int,
            right_limit: int,
            lines: List[int]
        ):
            if col_limit == limit:
                return [lines]

            ans = []
            candidates = ~(col_limit | left_limit | right_limit) & limit
            while candidates:
                right_one = candidates & (~candidates + 1)
                candidates = candidates - right_one
                ans += process(
                    limit,
                    col_limit | right_one,
                    (left_limit | right_one) << 1,
                    (right_limit | right_one) >> 1,
                    [*lines, bin(right_one)[2:].rjust(n, ".").replace("0", ".").replace("1", "Q")]
                )
            return ans

        limit = int("1" * n, 2)
        ans = process(limit, 0, 0, 0, [])
        return ans


class Tester(unittest.TestCase):

    def test_solution(self):
        import time
        obj = NQueues()
        s1_cost = 0
        s2_cost = 0
        for n in range(1, 13):
            s1 = time.perf_counter()
            ans1 = set(["".join(x) for x in obj.solution1(n)])
            s1_cost += time.perf_counter() - s1
            s2 = time.perf_counter()
            ans2 = set(["".join(x) for x in obj.solution2(n)])
            s2_cost += time.perf_counter() - s2
            self.assertEqual(ans1, ans2)
        print(f"solution1 cost: {s1_cost}")
        print(f"solution2 cost: {s2_cost}")


if __name__ == "__main__":
    unittest.main()
