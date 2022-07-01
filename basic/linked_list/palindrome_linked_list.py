#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest

from utils import Node, random_array, array_to_linked_list, linked_list_to_string


class PalindromeLinkedList:
    """
    ref: https://leetcode.cn/problems/palindrome-linked-list/
    """

    def solution1(self, head: Node) -> bool:
        stack = []
        # 进栈
        tmp = head
        while tmp:
            stack.append(tmp)
            tmp = tmp.next

        while stack:
            node = stack.pop()
            if node.val != head.val:
                return False
            head = head.next

        return True

    def solution2(self, head: Node) -> bool:
        if not head or not head.next:
            return True

        def reverse(cur: None):
            prev, next = None, None
            while cur is not None:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev

        # 快慢指针找前半部分链表的尾结点
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 反转后半部分链表
        prev = reverse(cur=slow.next)

        ans = True
        end = prev
        while ans and end is not None:
            if head.val != end.val:
                ans = False  # 不能直接反回, 需要恢复链表
            head = head.next
            end = end.next

        # 恢复后半部分链表
        reverse(cur=prev)

        return ans


class Tester(unittest.TestCase):

    def test_palindrome_linked_list(self):
        obj = PalindromeLinkedList()
        for _ in range(10000):
            array = random_array(min_size=0, max_size=100, min_value=0, max_value=9999)
            if random.random() < 0.5:
                if random.random() < 0.5:
                    array = array + array[::-1]
                else:
                    array = array + array[::-1][1:]
            gt = True if array == array[::-1] else False
            head = array_to_linked_list(array)
            original_str = linked_list_to_string(head, "")
            head_copy = head
            self.assertEqual(obj.solution1(head), gt)
            self.assertEqual(obj.solution2(head), gt, array)
            ans_str = linked_list_to_string(head_copy, "")
            self.assertEqual(original_str, ans_str)


if __name__ == "__main__":
    unittest.main()
