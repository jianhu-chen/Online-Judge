#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (38.25%)
# Likes:    649
# Dislikes: 0
# Total Accepted:    64.1K
# Total Submissions: 167.6K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
# 
# 示例：
# 
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 
# 说明：
# 
# 
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        valid = 0
        need = {}
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1
        window = {c: 0 for c in need}
        # 记录最小覆盖子串的起始索引及长度
        start, length = 0, float("INF")

        while right < len(s):
            # 增大窗口
            c = s[right]
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # 判断左侧窗口是否要收缩
            while valid == len(need):
                # 这里更新最小覆盖子串
                if right - left < length:
                    start = left
                    length = right - left
                # 将要移除的字符
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        return "" if length == float("INF") else s[start: start + length]

# @lc code=end

