# -*- encoding: utf-8 -*-
'''
@File    :   371.sum-of-two-integers.py
@Time    :   2020/02/06 22:29:15
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=371 lang=python
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0x100000000 # 2^32
        MAX_INT = 0x7FFFFFFF # int max
        MIN_INT = MAX_INT + 1
        while b != 0:
            temp = (a ^ b) % MASK
            b = ((a & b) << 1) % MASK
            a = temp
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)   

# @lc code=end

