# -*- encoding: utf-8 -*-
'''
@File    :   290.word-pattern.py
@Time    :   2020/02/02 14:07:34
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=290 lang=python
#
# [290] Word Pattern
#

# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        hash_table = dict()
        str_list = str.split()
        if len(str_list) != len(pattern):
            return False
        for p, s in zip(pattern, str_list):
            if p not in hash_table:
                hash_table[p] = s
            elif hash_table[p] != s:
                return False
        if len(hash_table) != len(set(str_list)):
            return False
        return True

# @lc code=end

