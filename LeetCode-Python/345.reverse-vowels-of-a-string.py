# -*- encoding: utf-8 -*-
'''
@File    :   345.reverse-vowels-of-a-string.py
@Time    :   2020/02/05 23:26:40
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=345 lang=python
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        char_stack = []
        idx_queue = []
        for idx, ch in enumerate(s):
            if ch.lower() in ["a", "e", "i", "o", "u"]:
                char_stack.append(ch)
                idx_queue.append(idx)
            result.append(ch)

        while char_stack:
            ch = char_stack.pop()
            idx = idx_queue.pop(0)
            result[idx] = ch
        return "".join(result)
# @lc code=end

