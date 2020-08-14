/*
 * @lc app=leetcode.cn id=72 lang=cpp
 *
 * [72] 编辑距离
 *
 * https://leetcode-cn.com/problems/edit-distance/description/
 *
 * algorithms
 * Hard (59.30%)
 * Likes:    1033
 * Dislikes: 0
 * Total Accepted:    74.4K
 * Total Submissions: 124.5K
 * Testcase Example:  '"horse"\n"ros"'
 *
 * 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
 * 
 * 你可以对一个单词进行如下三种操作：
 * 
 * 
 * 插入一个字符
 * 删除一个字符
 * 替换一个字符
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：word1 = "horse", word2 = "ros"
 * 输出：3
 * 解释：
 * horse -> rorse (将 'h' 替换为 'r')
 * rorse -> rose (删除 'r')
 * rose -> ros (删除 'e')
 * 
 * 
 * 示例 2：
 * 
 * 输入：word1 = "intention", word2 = "execution"
 * 输出：5
 * 解释：
 * intention -> inention (删除 't')
 * inention -> enention (将 'i' 替换为 'e')
 * enention -> exention (将 'n' 替换为 'x')
 * exention -> exection (将 'n' 替换为 'c')
 * exection -> execution (插入 'u')
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
    int dp(int i, int j, string word1, string word2)
    {
        // Base case
        if (i == -1)
        {
            return j + 1;
        }
        if (j == -1)
        {
            return i + 1;
        }

        if (word1[i] == word2[j])
        {
            return dp(i - 1, j - 1, word1, word2);
        }
        else
        {
            pair<int, int> ins(i, j-1);
            if 
            int ins = dp(i, j - 1, word1, word2) + 1;
            int del = dp(i - 1, j, word1, word2) + 1;
            int rep = dp(i - 1, j - 1, word1, word2) + 1;
            int min = (ins < del) ? ins : del;
            min = (rep < min) ? rep : min;
            return min;
        }
    }

    int minDistance(string word1, string word2)
    {
        return dp(word1.size() - 1, word2.size() - 1, word1, word2);
    }

private:
    map<pair<int, int>, int> mem;
};
// @lc code=end
