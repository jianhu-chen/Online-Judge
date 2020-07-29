/*
 * @lc app=leetcode.cn id=300 lang=cpp
 *
 * [300] 最长上升子序列
 *
 * https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
 *
 * algorithms
 * Medium (44.83%)
 * Likes:    846
 * Dislikes: 0
 * Total Accepted:    120.4K
 * Total Submissions: 268.2K
 * Testcase Example:  '[10,9,2,5,3,7,101,18]'
 *
 * 给定一个无序的整数数组，找到其中最长上升子序列的长度。
 * 
 * 示例:
 * 
 * 输入: [10,9,2,5,3,7,101,18]
 * 输出: 4 
 * 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
 * 
 * 说明:
 * 
 * 
 * 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
 * 你算法的时间复杂度应该为 O(n^2) 。
 * 
 * 
 * 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
 * 
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int lengthOfLIS(vector<int> &nums)
    {
        if (nums.size() == 0)
        {
            return 0;
        }
        vector<int> dp(nums.size(), 1);
        for (int i = 1; i < nums.size(); ++i)
        {
            for (int j = 0; j < i; ++j)
            {
                if (nums[i] > nums[j])
                {
                    dp[i] = max(dp[j] + 1, dp[i]);
                }
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};
// @lc code=end
