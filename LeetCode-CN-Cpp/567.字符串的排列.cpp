/*
 * @lc app=leetcode.cn id=567 lang=cpp
 *
 * [567] 字符串的排列
 *
 * https://leetcode-cn.com/problems/permutation-in-string/description/
 *
 * algorithms
 * Medium (36.56%)
 * Likes:    156
 * Dislikes: 0
 * Total Accepted:    34.9K
 * Total Submissions: 95.5K
 * Testcase Example:  '"ab"\n"eidbaooo"'
 *
 * 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
 * 
 * 换句话说，第一个字符串的排列之一是第二个字符串的子串。
 * 
 * 示例1:
 * 
 * 
 * 输入: s1 = "ab" s2 = "eidbaooo"
 * 输出: True
 * 解释: s2 包含 s1 的排列之一 ("ba").
 * 
 * 
 * 
 * 
 * 示例2:
 * 
 * 
 * 输入: s1= "ab" s2 = "eidboaoo"
 * 输出: False
 * 
 * 
 * 
 * 
 * 注意：
 * 
 * 
 * 输入的字符串只包含小写字母
 * 两个字符串的长度都在 [1, 10,000] 之间
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
    bool checkInclusion(string s1, string s2)
    {
        map<char, int> window;
        map<char, int> need;
        int valid = 0;

        for (int i = 0; i < s1.length(); ++i)
        {
            if (need.find(s1[i]) == need.end())
            {
                need.insert(pair<char, int>(s1[i], 1));
            }
            else
            {
                need[s1[i]]++;
            }
            if (window.find(s1[i]) == window.end())
            {
                window.insert(pair<char, int>(s1[i], 0));
            }
        }

        int left = 0, right = 0;
        while (right < s2.size())
        {
            char c = s2[right];
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
                if (right - left == s1.length())
                {
                    return true;
                }

                char d = s2[left];
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

        return false;
    }
};
// @lc code=end
