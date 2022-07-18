#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import List


class BestArrange:
    """
    安排会议室的最佳安排

    假设你有 1 个会议室，给你一个项目列表 programs, 每个元素包含会议的开始时间和结束时间，
    你可以按任意顺序安排这些会议室。返回最多可以安排的会议数目。
    """

    def solution1(self, programs: List[int]):
        """暴力解."""
        ans = 0
        num_methods = 1 << len(programs)
        for i in range(num_methods):
            selected = [programs[i] for i, x in enumerate(bin(i)[2:][::-1]) if x == '1']
            bad_method = False
            for check_idx in range(1, len(selected)):
                if bad_method:
                    break
                for prev_idx in range(check_idx):
                    cond1 = selected[prev_idx][0] < selected[check_idx][0] < selected[prev_idx][1]
                    cond2 = selected[prev_idx][0] < selected[check_idx][1] < selected[prev_idx][1]
                    cond3 = (
                        selected[check_idx][0] <= selected[prev_idx][0] and  # noqa: W504
                        selected[check_idx][1] >= selected[prev_idx][1]
                    )
                    if cond1 or cond2 or cond3:
                        bad_method = True
                        break
            if not bad_method:
                ans = max(ans, len(selected))
        return ans

    def solution2(self, programs: List[int]):
        """贪心."""
        programs.sort(key=lambda x: x[1])  # 按会议结束时间升序排列
        selected = []
        for i in range(len(programs)):
            if not selected or programs[i][0] >= selected[-1][1]:
                selected.append(programs[i])
        return len(selected)


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = BestArrange()
        for _ in range(100):
            programs = []
            for _ in range(random.randint(1, 20)):
                start = random.randint(0, 23)
                end = random.randint(start + 1, 24)
                programs.append((start, end))
            ans1 = obj.solution1(programs)
            ans2 = obj.solution2(programs)
            self.assertEqual(ans1, ans2, programs)


if __name__ == "__main__":
    unittest.main()
