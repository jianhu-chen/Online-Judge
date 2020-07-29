/*
 * @lc app=leetcode.cn id=46 lang=cpp
 *
 * [46] 全排列
 *
 * https://leetcode-cn.com/problems/permutations/description/
 *
 * algorithms
 * Medium (76.48%)
 * Likes:    792
 * Dislikes: 0
 * Total Accepted:    154.8K
 * Total Submissions: 202.4K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
 * 
 * 示例:
 * 
 * 输入: [1,2,3]
 * 输出:
 * [
 * ⁠ [1,2,3],
 * ⁠ [1,3,2],
 * ⁠ [2,1,3],
 * ⁠ [2,3,1],
 * ⁠ [3,1,2],
 * ⁠ [3,2,1]
 * ]
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
    void backtrack(vector<int> track, vector<int> nums)
    {
        // 判断是否满足结束条件
        if (track.size() == nums.size())
        {
            ret.push_back(track);
            return;
        }

        for (auto it = nums.begin(); it != nums.end(); ++it)
        {
            if (find(track.begin(), track.end(), *it) != track.end())
            {
                continue;
            }
            track.push_back(*it);
            backtrack(track, nums);
            track.pop_back();
        }
    }

    vector<vector<int>> permute(vector<int> &nums)
    {
        vector<int> track;
        backtrack(track, nums);
        return ret;
    }

private:
    vector<vector<int>> ret;
};
// @lc code=end
