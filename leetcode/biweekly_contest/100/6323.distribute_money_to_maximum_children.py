#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/distribute-money-to-maximum-children

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        d, m = divmod(money - children, 7)
        if d > children:
            return children - 1
        if d == children:
            return d if m == 0 else d - 1
        if d == children - 1 and m == 3:
            return d - 1
        return d
