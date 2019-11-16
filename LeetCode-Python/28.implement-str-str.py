# -*- encoding: utf-8 -*-
'''
@File    :   28.implement-str-str.py
@Time    :   2019/11/16 23:10:05
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=28 lang=python
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (33.18%)
# Likes:    1124
# Dislikes: 1559
# Total Accepted:    525.1K
# Total Submissions: 1.6M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
# Example 1:
#
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
#
# Example 2:
#
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
#
#

# @lc code=start


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        i = 0
        while i < len(haystack):
            if len(haystack[i:]) < len(needle):
                return -1
            if haystack[i] == needle[0]:
                p = i
                q = 0
                while p < len(haystack) and q < len(needle):
                    if haystack[p] != needle[q]:
                        break
                    if q == len(needle) - 1:
                        return i
                    p += 1
                    q += 1
            i += 1

        return -1
# @lc code=end


print(Solution().strStr("mississippi", "issip"))
print(Solution().strStr("a", "a"))
