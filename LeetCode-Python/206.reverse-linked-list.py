# -*- encoding: utf-8 -*-
'''
@File    :   206.reverse-linked-list.py
@Time    :   2020/01/31 16:48:44
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   None
'''
#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # def reverseList(self, head):
    #     """方法一：O(n) and O(1)
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if not head or not head.next:
    #         return head
    #     node_list = list()
    #     while head:
    #         node_list.append(head)
    #         head = head.next
    #     node_list.reverse()
    #     for idx, node in enumerate(node_list):
    #         if idx < len(node_list) - 1:
    #             node.next = node_list[idx+1]
    #     node_list[-1].next = None
    #     return node_list[0]

    def reverseList(self, head):
        """方法二：O(n) and O(1)
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
if __name__ == "__main__":
    node_list = list()
    for i in [1,2,3,4,5]:
        node = ListNode(i)
        node_list.append(node)
    
    for idx, node in enumerate(node_list):
        if idx < len(node_list) - 1:
            node.next = node_list[idx+1]
    
    head = node_list[0]
    head = Solution().reverseList(head)
    while head:
        print(head.val, end=" ")
        head = head.next