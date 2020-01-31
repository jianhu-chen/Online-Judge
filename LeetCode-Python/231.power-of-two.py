# -*- encoding: utf-8 -*-
'''
@File    :   231.power-of-two.py
@Time    :   2020/01/31 16:49:08
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=231 lang=python
#
# [231] Power of Two
#

# @lc code=start
from math import log
class Solution(object):
    def isPowerOfTwo(self, n):
        """方法一
        :type n: int
        :rtype: bool
        """
        return True if n > 0 and 2 ** int(log(n, 2)) == n else False
    
    def isPowerOfTwo(self, n):
        """方法二
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count == 1

# @lc code=end

