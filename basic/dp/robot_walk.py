#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import unittest


class RobotWalk:
    """
    假设有排成一行的N个位置记为1~N, N一定大于或等于2
    开始时机器人在其中的M位置上(M一定是1~N中的一个)
    如果机器人来到1位置, 那么下一步只能往右来到2位置;
    如果机器人来到N位置, 那么下一步只能往左来到N-1位置;
    如果机器人来到中间位置, 那么下一步可以往左走或者往右走;
    规定机器人必须走K步, 最终能来到P位置(P也是1~N中的一个)的方法有多少种
    给定四个参数 N、M、K、P, 返回方法数
    """

    def solution_recursion(self, N, rest, start, end):
        if N < 2 or start < 1 or start > N or end < 1 or end > N:
            return -1

        def recursion_process(N, rest, start, end):
            if rest == 0:
                return 1 if start == end else 0

            if start == 1:
                return recursion_process(N, rest - 1, start + 1, end)
            elif start == N:
                return recursion_process(N, rest - 1, start - 1, end)
            else:
                return recursion_process(N, rest - 1, start + 1, end) + \
                    recursion_process(N, rest - 1, start - 1, end)

        return recursion_process(N, rest, start, end)

    def solution_memory_search(self, N, rest, start, end):
        if N < 2 or start < 1 or start > N or end < 1 or end > N:
            return -1

        def memory_search_process(N, rest, start, end, dp):
            if dp[rest][start] != -1:
                return dp[rest][start]

            if rest == 0:
                ans = 1 if start == end else 0
            elif start == 1:
                ans = memory_search_process(N, rest - 1, start + 1, end, dp)
            elif start == N:
                ans = memory_search_process(N, rest - 1, start - 1, end, dp)
            else:
                ans = memory_search_process(N, rest - 1, start + 1, end, dp) + \
                    memory_search_process(N, rest - 1, start - 1, end, dp)
            dp[rest][start] = ans

            return ans

        # row (rest) range: [0, rest], col(start) range: [1, N]
        dp = [[-1 for _ in range(N + 1)] for _ in range(rest + 1)]
        return memory_search_process(N, rest, start, end, dp)

    def solution_dp(self, N, rest, start, end):
        if N < 2 or start < 1 or start > N or end < 1 or end > N:
            return -1

        # row (rest) range: [0, rest], col(start) range: [1, N]
        dp = [[0 for _ in range(N + 1)] for _ in range(rest + 1)]
        dp[0][end] = 1
        for i in range(1, rest + 1):
            for j in range(1, N + 1):
                if j != 1:
                    dp[i][j] += dp[i - 1][j - 1]
                if j != N:
                    dp[i][j] += dp[i - 1][j + 1]

        return dp[rest][start]


class TestRobotWalk(unittest.TestCase):

    def test_solution(self):
        TEST_TIMES = 1000
        obj = RobotWalk()
        s1_cost = 0
        s2_cost = 0
        s3_cost = 0
        for _ in range(TEST_TIMES):
            N = random.randint(2, 10)
            rest = random.randint(1, 2 * N)  # range: [1, 2 * N]
            start = random.randint(1, N)  # range: [1, N]
            end = random.randint(1, N)  # range: [1, N]
            args = (N, rest, start, end)
            s = time.perf_counter()
            A = obj.solution_recursion(*args)
            s1_cost += time.perf_counter() - s
            s = time.perf_counter()
            B = obj.solution_memory_search(*args)
            s2_cost += time.perf_counter() - s
            s = time.perf_counter()
            C = obj.solution_dp(*args)
            s3_cost += time.perf_counter() - s
            self.assertEqual(A, B, args)
            self.assertEqual(B, C, args)
        print("solution1 cost: {}".format(s1_cost))
        print("solution2 cost: {}".format(s2_cost))
        print("solution3 cost: {}".format(s3_cost))


if __name__ == '__main__':
    unittest.main()
