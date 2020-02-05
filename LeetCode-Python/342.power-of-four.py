# -*- encoding: utf-8 -*-
'''
@File    :   342.power-of-four.py
@Time    :   2020/02/05 23:16:53
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=342 lang=python
#
# [342] Power of Four
#

# @lc code=start
from math import log10
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type num: int
        :rtype: bool
        """
        """方法1：暴力法
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n < 1:
            return False
        return self.isPowerOfFour(n/4.0)

    def isPowerOfFour(self, n):
        """方法2
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        if log10(n) / log10(4) % 1 == 0:
            return True
        return False
        
# @lc code=end

