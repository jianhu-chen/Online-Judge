/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 *
 * https://leetcode-cn.com/problems/two-sum/description/
 *
 * algorithms
 * Easy (49.03%)
 * Likes:    8679
 * Dislikes: 0
 * Total Accepted:    1.2M
 * Total Submissions: 2.5M
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
 * 
 * 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
 * 
 * 
 * 
 * 示例:
 * 
 * 给定 nums = [2, 7, 11, 15], target = 9
 * 
 * 因为 nums[0] + nums[1] = 2 + 7 = 9
 * 所以返回 [0, 1]
 * 
 * 
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> ret;

        map<int, int> mem;
        for (int i = 0; i < nums.size(); ++i)
        {
            auto pos = mem.find(target - nums[i]);
            if (pos != mem.end())
            {
                ret.push_back(pos->second);
                ret.push_back(i);
                break;
            }
            else
            {
                mem.insert(pair<int, int>(nums[i], i));
            }
        }
        return ret;
    }
};
// @lc code=end

int main()
{
    Solution *s = NULL;
    vector<int> nums;
    nums.push_back(2);
    nums.push_back(7);
    nums.push_back(11);
    nums.push_back(15);
    vector<int> ret = s->twoSum(nums, 9);
    for (int i = 0; i < ret.size(); ++i)
    {
        cout << ret[i] << endl;
    }
    system("pause");
}
