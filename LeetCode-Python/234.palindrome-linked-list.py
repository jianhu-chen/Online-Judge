# -*- encoding: utf-8 -*-
'''
@File    :   234.palindrome-linked-list.py
@Time    :   2020/01/31 17:17:04
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
#     def isPalindrome(self, head):
#         """方法一：O(n) and O(n)
#         :type head: ListNode
#         :rtype: bool
#         """
#         node_list = self.getNodeList(head)
#         for idx in range(int(len(node_list)*0.5)):
#             if node_list[idx].val != node_list[-idx-1].val:
#                 return False
#         return True

#     def getNodeList(self, head):
#         node = head
#         result = []
#         while node:
#             result.append(node)
#             node = node.next
#         return result

class Solution(object):
    def isPalindrome(self, head):
        """方法二：翻转后半部分链表 O(n) and O(1)
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        first_half_end = self.end_of_first_half(head)
        last_half_head = self.reverse_list(first_half_end.next)
        first_half_head = head
        while first_half_head and last_half_head:
            if first_half_head.val != last_half_head.val:
                return False
            first_half_head = first_half_head.next
            last_half_head = last_half_head.next
        return True

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse_list(self, head):
        """O(n) and O(1)
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        left = head
        right = left.next
        next = right.next
        head.next = None
        while next:
            right.next = left
            left = right
            right = next
            next = next.next
        right.next = left
        return right

        
# @lc code=end

