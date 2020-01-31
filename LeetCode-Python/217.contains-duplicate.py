#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    # def containsDuplicate(self, nums):
    #     """方法一
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     return False if len(set(nums)) == len(nums) else True
    
    def containsDuplicate(self, nums):
        """方法二：hash table O(n) and O(n)
        :type nums: List[int]
        :rtype: bool
        """
        hash_table = dict()
        # 这里把dict改成list就会超时，应该是dict和list的底层设计不一样，
        # dict的查找时间会快一些
        for n in nums:
            if n in hash_table:
                return True
            else:
                hash_table[n] = 1
        return False
        
    # def containsDuplicate(self, nums):
    #     """方法三：线性查找 O(n^2)超时 and O(1)
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     for n in nums:
    #         if nums.count(n) > 1:
    #             return True
    #     return False
    
    # def containsDuplicate(self, nums):
    #     """方法四：先排序 再查找 O(nlogn) and O(1)
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     nums.sort()
    #     for idx, n in enumerate(nums):
    #         if idx < len(nums) - 1 and n == nums[idx+1]:
    #             return True
    #     return False
# @lc code=end

