# -*- encoding: utf-8 -*-
'''
@File    :   205.isomorphic-strings.py
@Time    :   2020/01/31 12:22:27
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_table = dict()
        for s_c, t_c in zip(s, t):
            if s_c not in hash_table:
                hash_table[s_c] = t_c
            else:
                if hash_table[s_c] != t_c:
                    return False
        hash_table_values = hash_table.values()
        if len(set(hash_table_values)) == len(hash_table_values):
            return True
        else:
            return False
        
# @lc code=end

