#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (48.46%)
# Likes:    334
# Dislikes: 0
# Total Accepted:    42.3K
# Total Submissions: 87.1K
# Testcase Example:  '[1,5,11,5]'
#
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
# 注意:
#
#
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
#
#
# 示例 1:
#
# 输入: [1, 5, 11, 5]
#
# 输出: true
#
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
#
#
#
#
# 示例 2:
#
# 输入: [1, 2, 3, 5]
#
# 输出: false
#
# 解释: 数组不能分割成两个元素和相等的子集.
#
#
#
#
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        转换为0-1背包问题, 动态规划, O(N^2)
        """
        if not nums:
            return False

        s = sum(nums)
        if s % 2 == 0:
            half_s = s // 2
        else:
            return False

        # Base case
        # dp[i][j] = x 表示, 对于前 i 个物品, 当前背包的容量为 j 时, 若 x 为 true,
        # 则说明可以恰好将背包装满, 若 x 为 false, 则说明不能恰好将背包装满。
        dp = [[False for _ in range(half_s+1)] for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            dp[i][0] = True

        for i in range(1, len(nums)+1):
            for j in range(1, half_s+1):
                if nums[i-1] > j:
                    # 不装入
                    dp[i][j] = dp[i-1][j]
                else:
                    # 不装入 or 装入
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[-1][-1]
# @lc code=end
