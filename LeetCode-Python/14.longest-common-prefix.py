# -*- encoding: utf-8 -*-
'''
@File    :   14.longest-common-prefix.py
@Time    :   2019/11/16 16:55:48
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.31%)
# Likes:    1732
# Dislikes: 1542
# Total Accepted:    582K
# Total Submissions: 1.7M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#
#

# @lc code=start


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        strs.sort()
        result = strs[0]
        for i in range(1, len(strs)):
            for j in range(min(len(strs[i]), len(result))):
                # result = result[:len(strs[i])]
                if result[j] != strs[i][j]:
                    result = result[:j]
                    break

        return result

# @lc code=end
