#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import unittest

from basic.dp import RobotWalk, CardsInLine

TEST_TIMES = 100  # 1k times test


class TestDP(unittest.TestCase):

    def test_robot_walk(self):
        obj = RobotWalk()
        for _ in range(TEST_TIMES):
            N = random.randint(2, 10)
            rest = random.randint(1, 2 * N)  # range: [1, 2 * N]
            start = random.randint(1, N)  # range: [1, N]
            end = random.randint(1, N)  # range: [1, N]
            args = (N, rest, start, end)
            A = obj.solution_recursion(*args)
            B = obj.solution_memory_search(*args)
            C = obj.solution_dp(*args)
            self.assertEqual(A, B, args)
            self.assertEqual(B, C, args)

    def test_cards_in_line(self):
        obj = CardsInLine()
        for _ in range(TEST_TIMES):
            arr = list(range(1, 100))
            random.shuffle(arr)
            arr = arr[0:random.randint(1, 20)]
            A = obj.solution_recursion(arr)
            B = obj.solution_memory_search(arr)
            C = obj.solution_dp(arr)
            self.assertEqual(A, B, arr)
            self.assertEqual(B, C, arr)
