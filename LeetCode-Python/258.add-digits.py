# -*- encoding: utf-8 -*-
'''
@File    :   258.add-digits.py
@Time    :   2020/02/01 14:50:07
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=258 lang=python
#
# [258] Add Digits
#

# @lc code=start
class Solution(object):
    def addDigits(self, num):
        """O(1)
        ref:
            https://leetcode-cn.com/problems/add-digits/solution/o1-by-user682/
        :type num: int
        :rtype: int
        """
        return 0 if num == 0 else (num - 1) % 9 + 1
        
# @lc code=end

