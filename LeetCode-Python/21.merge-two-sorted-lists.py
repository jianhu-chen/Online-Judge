# -*- encoding: utf-8 -*-
'''
@File    :   21.merge-two-sorted-lists.py
@Time    :   2019/11/16 17:44:54
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (49.71%)
# Likes:    2901
# Dislikes: 420
# Total Accepted:    746.3K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#
#

# @lc code=start
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pRoot = pCurr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                pCurr.next = l1
                l1 = l1.next
            else:
                pCurr.next = l2
                l2 = l2.next
            pCurr = pCurr.next

        while l1:
            pCurr.next = l1
            l1 = l1.next
            pCurr = pCurr.next

        while l2:
            pCurr.next = l2
            l2 = l2.next
            pCurr = pCurr.next

        return pRoot.next
# @lc code=end
