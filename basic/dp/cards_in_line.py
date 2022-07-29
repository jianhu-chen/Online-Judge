#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import unittest


class CardsInLine:
    """
    给定一个整型数组arr, 代表数值不同的纸牌排成一条线
    玩家A和玩家B依次拿走每张纸牌
    规定玩家A先拿, 玩家B后拿
    但是每个玩家每次只能拿走最左或最右的纸牌
    玩家A和玩家B都绝顶聪明
    请返回最后获胜者的分数
    """

    def solution_recursion(self, arr):
        if not arr:
            return 0

        def recursion_first_select(arr, start, end):
            if start == end:
                return arr[start]
            return max(
                recursion_second_select(arr, start + 1, end) + arr[start],
                recursion_second_select(arr, start, end - 1) + arr[end],
            )

        def recursion_second_select(arr, start, end):
            if start == end:
                return 0
            return min(
                recursion_first_select(arr, start + 1, end),
                recursion_first_select(arr, start, end - 1),
            )

        first_select = recursion_first_select(arr, 0, len(arr) - 1)
        second_secect = recursion_second_select(arr, 0, len(arr) - 1)
        return max(first_select, second_secect)

    def solution_memory_search(self, arr):
        if not arr:
            return 0

        def memory_search_first_select(arr, start, end, dp1, dp2):
            if dp1[start][end] != -1:
                return dp1[start][end]

            if start == end:
                ans = arr[start]
            else:
                ans = max(
                    memory_search_second_select(arr, start + 1, end, dp1, dp2) + arr[start],
                    memory_search_second_select(arr, start, end - 1, dp1, dp2) + arr[end]
                )
            dp1[start][end] = ans
            return ans

        def memory_search_second_select(arr, start, end, dp1, dp2):
            if dp2[start][end] != -1:
                return dp2[start][end]

            if start == end:
                ans = 0
            else:
                ans = min(
                    memory_search_first_select(arr, start + 1, end, dp1, dp2),
                    memory_search_first_select(arr, start, end - 1, dp1, dp2)
                )
            dp2[start][end] = ans
            return ans

        # row (rest) range: [0, len(arr) - 1], col(start) range: [0, len(arr) - 1]
        dp1 = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
        dp2 = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
        first_select = memory_search_first_select(arr, 0, len(arr) - 1, dp1, dp2)
        second_secect = memory_search_second_select(arr, 0, len(arr) - 1, dp1, dp2)
        return max(first_select, second_secect)

    def solution_dp(self, arr):
        if not arr:
            return 0

        # row (rest) range: [0, len(arr) - 1], col(start) range: [0, len(arr) - 1]
        dp1 = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
        dp2 = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
        for i in range(len(arr)):
            dp1[i][i] = arr[i]
            dp2[i][i] = 0

        for diff in range(1, len(arr)):
            for i in range(0, len(arr) - diff):
                j = i + diff
                dp1[i][j] = max(dp2[i + 1][j] + arr[i], dp2[i][j - 1] + arr[j])
                dp2[i][j] = min(dp1[i][j - 1], dp1[i + 1][j])

        return max(dp1[0][len(arr) - 1], dp2[0][len(arr) - 1])


class TestCardsInLine(unittest.TestCase):

    def test_solution(self):
        TEST_TIMES = 10
        obj = CardsInLine()
        s1_cost, s2_cost, s3_cost = 0, 0, 0
        for _ in range(TEST_TIMES):
            arr = list(range(1, 100))
            random.shuffle(arr)
            arr = arr[0:random.randint(1, 25)]
            s = time.perf_counter()
            A = obj.solution_recursion(arr)
            s1_cost += time.perf_counter() - s
            s = time.perf_counter()
            B = obj.solution_memory_search(arr)
            s2_cost += time.perf_counter() - s
            s = time.perf_counter()
            C = obj.solution_dp(arr)
            s3_cost += time.perf_counter() - s
            self.assertEqual(A, B, arr)
            self.assertEqual(B, C, arr)
        print("solution1 cost: {}".format(s1_cost))
        print("solution2 cost: {}".format(s2_cost))
        print("solution3 cost: {}".format(s3_cost))


if __name__ == '__main__':
    unittest.main()
