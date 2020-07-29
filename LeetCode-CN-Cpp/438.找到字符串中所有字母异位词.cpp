/*
 * @lc app=leetcode.cn id=438 lang=cpp
 *
 * [438] 找到字符串中所有字母异位词
 *
 * https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
 *
 * algorithms
 * Medium (45.27%)
 * Likes:    319
 * Dislikes: 0
 * Total Accepted:    32.2K
 * Total Submissions: 71K
 * Testcase Example:  '"cbaebabacd"\n"abc"'
 *
 * 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
 * 
 * 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
 * 
 * 说明：
 * 
 * 
 * 字母异位词指字母相同，但排列不同的字符串。
 * 不考虑答案输出的顺序。
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入:
 * s: "cbaebabacd" p: "abc"
 * 
 * 输出:
 * [0, 6]
 * 
 * 解释:
 * 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
 * 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入:
 * s: "abab" p: "ab"
 * 
 * 输出:
 * [0, 1, 2]
 * 
 * 解释:
 * 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
 * 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
 * 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
 * 
 * 
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

class Solution
{
public:
    vector<int> findAnagrams(string s, string p)
    {
        vector<int> ret;
        map<char, int> window;
        map<char, int> need;
        int valid = 0;

        for (int i = 0; i < p.length(); ++i)
        {
            if (need.find(p[i]) == need.end())
            {
                need.insert(pair<char, int>(p[i], 1));
            }
            else
            {
                need[p[i]]++;
            }
            if (window.find(p[i]) == window.end())
            {
                window.insert(pair<char, int>(p[i], 0));
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
                if (right - left == p.length())
                {
                    ret.push_back(left);
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

        return ret;
    }
};
// @lc code=end
