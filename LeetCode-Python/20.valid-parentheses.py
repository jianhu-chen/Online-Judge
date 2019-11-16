# -*- encoding: utf-8 -*-
'''
@File    :   20.valid-parentheses.py
@Time    :   2019/11/16 17:45:07
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (37.49%)
# Likes:    3610
# Dislikes: 175
# Total Accepted:    754.6K
# Total Submissions: 2M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#
#

# @lc code=start


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        pair = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = []
        for ch in s:
            if ch in pair.keys():
                stack.append(ch)
                continue
            if stack == [] or pair[stack[-1]] != ch:
                return False
            else:
                stack.pop()

        if stack == []:
            return True
        else:
            return False
# @lc code=end


# print(Solution().isValid('()[]{}'))
