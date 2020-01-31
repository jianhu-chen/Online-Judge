# -*- encoding: utf-8 -*-
'''
@File    :   242.valid-anagram.py
@Time    :   2020/01/31 18:56:15
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    # def isAnagram(self, s, t):
    #     """方法一：hash table
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     hash_table = dict()
    #     for s_c in s:
    #         if s_c not in hash_table:
    #             hash_table[s_c] = 1
    #         else:
    #             hash_table[s_c] += 1

    #     if len(hash_table) != len(set(t)):
    #         return False

    #     for t_c in set(t):
    #         if t_c not in hash_table:
    #             return False
    #         elif hash_table[t_c] != t.count(t_c):
    #             return False
    #     return True
                
    def isAnagram(self, s, t):
        """方法二：sort
        :type s: str
        :type t: str
        :rtype: bool
        """
        return ''.join(sorted(s)) == ''.join(sorted(t))
# @lc code=end

