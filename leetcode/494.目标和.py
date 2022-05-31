#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
# https://leetcode-cn.com/problems/target-sum/description/
#
# algorithms
# Medium (44.39%)
# Likes:    323
# Dislikes: 0
# Total Accepted:    35.7K
# Total Submissions: 80.5K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或
# -中选择一个符号添加在前面。
# 
# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
# 
# 
# 
# 示例：
# 
# 输入：nums: [1, 1, 1, 1, 1], S: 3
# 输出：5
# 解释：
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# 一共有5种方法让最终目标和为3。
# 
# 
# 
# 
# 提示：
# 
# 
# 数组非空，且长度不会超过 20 。
# 初始的数组的和不会超过 1000 。
# 保证返回的最终结果能被 32 位整数存下。
# 
# 
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        回溯法 O(2^N) 超时 ...
        """
        ret = 0
        def backtrack(idx: int, rest: int):
            nonlocal ret
            # 判断是否满足结束条件
            if idx == len(nums):
                if rest == 0:
                    ret += 1
                return

            # 做选择
            for sign in [1, -1]:
                backtrack(idx + 1, rest + sign * nums[idx])

        backtrack(0, S)
        return ret

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        回溯法 O(2^N) + 用备忘录消除处重叠子问题 ...
        """
        mem = {}
        def backtrack(idx: int, rest: int):
            # 判断是否满足结束条件
            if idx == len(nums):
                if rest == 0:
                    return 1
                return 0

            if (idx, rest) in mem:
                return mem[(idx, rest)]

            # 做选择
            result = 0
            for sign in [1, -1]:
                result += backtrack(idx + 1, rest + sign * nums[idx])

            mem[(idx, rest)] = result
            return result

        return backtrack(0, S)
# @lc code=end

