# -*- encoding: utf-8 -*-
'''
@File    :   263.ugly-number.py
@Time    :   2020/02/01 14:54:55
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=263 lang=python
#
# [263] Ugly Number
#

# @lc code=start
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        while num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            if num % 2 == 0:
                num //= 2
            if num % 3 == 0:
                num //= 3
            if num % 5 == 0:
                num //= 5
            if num == 1:
                return True
        return False
