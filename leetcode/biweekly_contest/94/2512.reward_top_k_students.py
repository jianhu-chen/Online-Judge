#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/reward-top-k-students
from typing import List


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        ps = set(positive_feedback)
        ns = set(negative_feedback)
        sid2score = {}
        for rep, sid in zip(report, student_id):
            score = 0
            for word in rep.split(" "):
                if word in ps:
                    score += 3
                elif word in ns:
                    score -= 1
            sid2score[sid] = score
        return [x[0] for x in sorted(sid2score.items(), key=lambda x: (-x[1], x[0]))[:k]]
