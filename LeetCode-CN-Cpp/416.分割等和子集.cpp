/*
 * @lc app=leetcode.cn id=416 lang=cpp
 *
 * [416] 分割等和子集
 *
 * https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
 *
 * algorithms
 * Medium (47.45%)
 * Likes:    350
 * Dislikes: 0
 * Total Accepted:    45.6K
 * Total Submissions: 93.6K
 * Testcase Example:  '[1,5,11,5]'
 *
 * 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
 * 
 * 注意:
 * 
 * 
 * 每个数组中的元素不会超过 100
 * 数组的大小不会超过 200
 * 
 * 
 * 示例 1:
 * 
 * 输入: [1, 5, 11, 5]
 * 
 * 输出: true
 * 
 * 解释: 数组可以分割成 [1, 5, 5] 和 [11].
 * 
 * 
 * 
 * 
 * 示例 2:
 * 
 * 输入: [1, 2, 3, 5]
 * 
 * 输出: false
 * 
 * 解释: 数组不能分割成两个元素和相等的子集.
 * 
 * 
 * 
 * 
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    bool canPartition(vector<int> &nums)
    {
        int sum = 0;
        for (int i = 0; i < nums.size(); ++i)
        {
            sum += nums[i];
        }

        if (sum % 2 != 0)
        {
            return false;
        }

        int half = sum / 2;

        vector<vector<bool>> dp(nums.size() + 1, vector<bool>(half + 1, false));
        for (int i = 0; i < nums.size() + 1; ++i)
        {
            dp[i][0] = true;
        }

        for (int i = 1; i < nums.size() + 1; ++i)
        {
            for (int j = 1; j < half + 1; ++j)
            {
                // 不装
                if (nums[i - 1] > j)
                {
                    dp[i][j] = dp[i - 1][j];
                }
                // 装 or 不装
                else
                {
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] || dp[i - 1][j];
                }
            }
        }
        return dp[nums.size()][half];
    }
};
// @lc code=end
