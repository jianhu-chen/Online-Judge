# -*- encoding: utf-8 -*-
'''
@File    :   141.linked-list-cycle.py
@Time    :   2019/11/19 23:40:14
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (38.61%)
# Likes:    1940
# Dislikes: 279
# Total Accepted:    489.5K
# Total Submissions: 1.3M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which
# represents the position (0-indexed) in the linked list where tail connects
# to. If pos is -1, then there is no cycle in the linked list.
#
#
#
#
# Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
#
#
#
#
#
#
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
#
#
#
#
#
#
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
#
#
#
#
#
# Follow up:
#
# Can you solve it using O(1) (i.e. constant) memory?
#
#

# @lc code=start
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法一：哈希表
# 我们遍历所有结点并在哈希表中存储每个结点的引用（或内存地址）。
# 如果当前结点为空结点 null（即已检测到链表尾部的下一个结点），
# 那么我们已经遍历完整个链表，并且该链表不是环形链表。
# 如果当前结点的引用已经存在于哈希表中，那么返回 true（即该链表为环形链表）。
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         if not head:
#             return False
#         hash_map = {}
#         while head:
#             try:
#                 hash_map.pop(head)
#                 return True
#             except:
#                 hash_map[head] = 1
#             head = head.next
#         return False

# 方法二：快慢指针


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        fast = head.next
        slow = head
        while fast != slow:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True
# @lc code=end
