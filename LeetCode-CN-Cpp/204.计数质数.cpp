/*
 * @lc app=leetcode.cn id=204 lang=cpp
 *
 * [204] 计数质数
 *
 * https://leetcode-cn.com/problems/count-primes/description/
 *
 * algorithms
 * Easy (34.88%)
 * Likes:    418
 * Dislikes: 0
 * Total Accepted:    72.3K
 * Total Submissions: 207.2K
 * Testcase Example:  '10'
 *
 * 统计所有小于非负整数 n 的质数的数量。
 * 
 * 示例:
 * 
 * 输入: 10
 * 输出: 4
 * 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
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
    int countPrimes(int n)
    {
        vector<bool> isPrim(n, true);
        for (int i = 2; i * i < n; i++)
        {
            if (isPrim[i])
            {
                for (int j = i * i; j < n; j += i)
                {
                    isPrim[j] = false;
                }
            }
        }

        int count = 0;
        for (int i = 2; i < n; i++)
        {
            if (isPrim[i])
            {
                count++;
            }
        }

        return count;
    }
};
// @lc code=end
