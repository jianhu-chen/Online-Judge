#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (76.48%)
# Likes:    792
# Dislikes: 0
# Total Accepted:    154.8K
# Total Submissions: 202.4K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#

# @lc code=start
import copy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtrack(nums, track):
            # 结束条件
            if len(track) == len(nums):
                ret.append(track)

            for num in nums:
                # 排除不合法的选择
                if num in track:
                    continue

                track_copy = copy.deepcopy(track)
                track_copy.append(num)
                backtrack(nums, track_copy)

        backtrack(nums, [])
        return ret

# @lc code=end
