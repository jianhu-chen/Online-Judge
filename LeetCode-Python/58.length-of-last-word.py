# -*- encoding: utf-8 -*-
'''
@File    :   58.length-of-last-word.py
@Time    :   2019/11/17 13:21:06
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.34%)
# Likes:    467
# Dislikes: 1938
# Total Accepted:    311.7K
# Total Submissions: 964K
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space
# characters only.
#
# Example:
#
#
# Input: "Hello World"
# Output: 5
#
#
#
#
#

# @lc code=start


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s.isspace():
            return 0
        words = s.split()
        if words[-1].isalpha():
            return len(words[-1])
        else:
            return 0

# @lc code=end
