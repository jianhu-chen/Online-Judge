#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (35.11%)
# Likes:    4002
# Dislikes: 0
# Total Accepted:    575.1K
# Total Submissions: 1.6M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        length = 0
        window = {c: 0 for c in set(s)}

        while right < len(s):
            # 增大窗口
            c = s[right]
            right += 1
            # 进行窗口内数据的一些列更新
            window[c] += 1

            # 缩小窗口
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1

            # 更新答案
            if right - left > length:
                length = right - left

        return length
# @lc code=end

