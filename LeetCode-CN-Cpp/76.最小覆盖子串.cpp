/*
 * @lc app=leetcode.cn id=76 lang=cpp
 *
 * [76] 最小覆盖子串
 *
 * https://leetcode-cn.com/problems/minimum-window-substring/description/
 *
 * algorithms
 * Hard (38.25%)
 * Likes:    649
 * Dislikes: 0
 * Total Accepted:    64.1K
 * Total Submissions: 167.6K
 * Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
 *
 * 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
 * 
 * 示例：
 * 
 * 输入: S = "ADOBECODEBANC", T = "ABC"
 * 输出: "BANC"
 * 
 * 说明：
 * 
 * 
 * 如果 S 中不存这样的子串，则返回空字符串 ""。
 * 如果 S 中存在这样的子串，我们保证它是唯一的答案。
 * 
 * 
 */

// @lc code=start
#include <iostream>
#include <string>
#include <map>

using namespace std;

class Solution
{
public:
    string minWindow(string s, string t)
    {
        map<char, int> window;
        map<char, int> need;
        int valid = 0;
        int start = 0, length = s.size() + 1;

        for (int i = 0; i < t.length(); ++i)
        {
            if (need.find(t[i]) == need.end())
            {
                need.insert(pair<char, int>(t[i], 1));
            }
            else
            {
                need[t[i]]++;
            }
            if (window.find(t[i]) == window.end())
            {
                window.insert(pair<char, int>(t[i], 0));
            }
        }

        int left = 0, right = 0;
        while (right < s.size())
        {
            char c = s[right];
            ++right;
            // 进行窗口内数据的一系列操作
            if (need.find(c) != need.end())
            {
                ++window[c];
                if (window[c] == need[c])
                {
                    ++valid;
                }
            }

            while (valid == need.size())
            {
                if (right - left < length)
                {
                    start = left;
                    length = right - left;
                }

                char d = s[left];
                ++left;
                // 进项窗口收缩后的一系列操作
                if (need.find(d) != need.end())
                {
                    if (window[d] == need[d])
                    {
                        --valid;
                    }
                    --window[d];
                }
            }
        }

        if (length == s.size() + 1)
        {
            return "";
        }
        else
        {
            return s.substr(start, length);
        }
    }
};
// @lc code=end
