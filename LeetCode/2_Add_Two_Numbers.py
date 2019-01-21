# -*- coding: utf-8 -*-
# @File 	: 2_Add_Two_Numbers.py
# @Author 	: jianhuChen
# @Date 	: 2019-01-21 11:39:35
# @License 	: Copyright(C), USTC
# @Last Modified by  : jianhuChen
# @Last Modified time: 2019-01-21 18:46:36



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        preNode = result
        carryFlag = 0
        while True:
            if l1 == None and l2 == None:
                if carryFlag:
                    node = ListNode(1)
                    preNode.next = node
                return result.next
            else:
                if l1 == None:
                    val = l2.val + carryFlag
                elif l2 == None:
                    val = l1.val + carryFlag
                else:
                    val = l1.val + l2.val + carryFlag
                if val>=10:
                    carryFlag = 1
                    val -= 10
                else:
                    carryFlag = 0
                node = ListNode(val)
                preNode.next = node
                preNode = node
                if l1 != None:
                    l1 = l1.next
                if l2 != None:
                    l2 = l2.next                
