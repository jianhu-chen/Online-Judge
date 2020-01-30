# -*- encoding: utf-8 -*-
'''
@File    :   203.remove-linked-list-elements.py
@Time    :   2020/01/30 23:05:17
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=203 lang=python
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """方法1：时间复杂度O(n) and 空间复杂度O(1)
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        pNode = head
        while pNode and pNode.next:
            if pNode.next.val == val:
                pNode.next = pNode.next.next
            else:
                pNode = pNode.next
        return head

    def removeElements(self, head, val):
        """方法2：O(n) and O(n)
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        pHead = ListNode('@')
        pNode = pHead
        while head:
            if head.val != val:
                pNode.next = ListNode(head.val)
                pNode = pNode.next
            head = head.next
        return pHead.next        
# @lc code=end

