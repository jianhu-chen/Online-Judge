# -*- encoding: utf-8 -*-
'''
@File    :   326.power-of-three.py
@Time    :   2020/02/02 14:32:35
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=326 lang=python
#
# [326] Power of Three
#

# @lc code=start
from math import log10

class Solution(object):
    def isPowerOfThree(self, n):
        """方法1：暴力法
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n < 1:
            return False
        return self.isPowerOfThree(n/3.0)

    def isPowerOfThree(self, n):
        """方法2
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        if log10(n) / log10(3) % 1 == 0:
            return True
        return False


# @lc code=end

