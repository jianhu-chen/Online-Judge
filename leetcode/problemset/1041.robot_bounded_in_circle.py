#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/robot-bounded-in-circle

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        distance = [0] * 4
        for i in instructions:
            if i == "G":
                distance[direction] += 1
            elif i == "L":
                direction = (direction + 3) % 4
            else:
                direction = (direction + 1) % 4
        return direction != 0 or (distance[0] == distance[2] and distance[1] == distance[3])
