#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from typing import List


class Hanota:
    """
    在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。
    一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。移动圆盘时受到以下限制:

    (1) 每次只能移动一个盘子;
    (2) 盘子只能从柱子顶端滑出移到下一根柱子;
    (3) 盘子只能叠在比它大的盘子上。

    请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。

    你需要原地修改栈。

    https://leetcode.cn/problems/hanota-lcci
    """

    def solution(self, A: List[int], B: List[int], C: List[int]) -> None:

        def move(n, src, des, oth):
            if n == 1:
                des.append(src.pop())
            else:
                move(n - 1, src, oth, des)
                des.append(src.pop())
                move(n - 1, oth, des, src)

        move(len(A), A, C, B)

    def print_solution(self, A: List[int], B: List[int], C: List[int]) -> None:

        def move(n, src, des, oth):
            src, nsrc = src
            des, ndes = des
            oth, noth = oth
            if n == 1:
                print("move {} from {} to {}".format(src[-1], nsrc, ndes))
                des.append(src.pop())
            else:
                move(n - 1, (src, nsrc), (oth, noth), (des, ndes))
                print("move {} from {} to {}".format(src[-1], nsrc, ndes))
                des.append(src.pop())
                move(n - 1, (oth, noth), (des, ndes), (src, nsrc))

        move(len(A), (A, "A"), (C, "C"), (B, "B"))


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = Hanota()
        for n in range(2, 25):
            A = [i for i in range(1, n)]
            B = []
            C = []
            obj.solution(A, B, C)
            self.assertEqual(A, [])
            self.assertEqual(B, [])
            self.assertEqual(C, [i for i in range(1, n)])


if __name__ == "__main__":
    Hanota().print_solution([3, 2, 1], [], [])
    unittest.main()
