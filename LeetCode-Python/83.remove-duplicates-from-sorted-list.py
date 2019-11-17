# -*- encoding: utf-8 -*-
'''
@File    :   83.remove-duplicates-from-sorted-list.py
@Time    :   2019/11/17 21:23:02
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=83 lang=python
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (43.64%)
# Likes:    984
# Dislikes: 88
# Total Accepted:    381.3K
# Total Submissions: 872.2K
# Testcase Example:  '[1,1,2]'
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
#
# Example 1:
#
#
# Input: 1->1->2
# Output: 1->2
#
#
# Example 2:
#
#
# Input: 1->1->2->3->3
# Output: 1->2->3
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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        pRoot = pCurr = ListNode(-99)
        while head:
            if head.val != pCurr.val:
                pCurr.next = head
                pCurr = pCurr.next
            head = head.next
        pCurr.next = None
        return pRoot.next
# @lc code=end
