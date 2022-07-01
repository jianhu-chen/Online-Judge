#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from utils import Node, random_array, array_to_linked_list


class LinkedListMid:
    """
    找到链表的中点.
    """

    def mid_or_up_mid_node(self, head: Node) -> Node:
        """
        1 -> 2 -> 3 return 2.
        1 -> 2 -> 3 -> 4 return 2.
        """
        if not head or not head.next:
            return head

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mid_or_down_mid_node(self, head: Node) -> Node:
        """
        1 -> 2 -> 3 return 2.
        1 -> 2 -> 3 -> 4 return 3.
        """
        if not head or not head.next:
            return head

        # !NOTE: 同时向后移动一个指针
        slow, fast = head.next, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mid_or_up_mid_pre_node(self, head: Node) -> Node:
        """
        1 -> 2 -> 3 return 1.
        1 -> 2 -> 3 -> 4 return 1.
        """
        if not head or not head.next or not head.next.next:
            return None

        # 大于等于3个节点
        slow, fast = head, head.next.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mid_or_down_mid_pre_node(self, head: Node) -> Node:
        """
        1 -> 2 -> 3 return 1.
        1 -> 2 -> 3 -> 4 return 2.
        """
        if not head or not head.next:
            return None

        if not head.next.next:
            return head

        # 大于等于3个节点
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mid_or_up_mid_next_node(self, head: Node) -> Node:
        """
        1 -> 2 -> 3 return 3.
        1 -> 2 -> 3 -> 4 return 3.
        """
        if not head or not head.next:
            return None

        if not head.next.next:
            return head.next

        # 大于等于3个节点
        slow, fast = head.next, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mid_or_down_mid_next_node(self, head: Node) -> Node:
        """
        1 -> 2 -> 3 return 3.
        1 -> 2 -> 3 -> 4 return 4.
        """
        if not head or not head.next or not head.next.next:
            return None

        # 大于等于3个节点
        slow, fast = head.next.next, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = LinkedListMid()
        for _ in range(10000):
            array = random_array(0, 100, 0, 100)
            head = array_to_linked_list(array)

            mid_val = array[(len(array) - 1) // 2] if array else None
            mid_node = obj.mid_or_up_mid_node(head)
            self.assertTrue(mid_val == mid_node or mid_val == mid_node.val)

            mid_val = array[len(array) // 2] if array else None
            mid_node = obj.mid_or_down_mid_node(head)
            self.assertTrue(mid_val == mid_node or mid_val == mid_node.val)

            mid_val = array[(len(array) - 1) // 2 - 1] if len(array) >= 3 else None
            mid_node = obj.mid_or_up_mid_pre_node(head)
            self.assertTrue(mid_val == mid_node or mid_val == mid_node.val)

            mid_val = array[len(array) // 2 - 1] if len(array) >= 2 else None
            mid_node = obj.mid_or_down_mid_pre_node(head)
            self.assertTrue(mid_val == mid_node or mid_val == mid_node.val)

            mid_val = array[(len(array) - 1) // 2 + 1] if len(array) >= 2 else None
            mid_node = obj.mid_or_up_mid_next_node(head)
            self.assertTrue(mid_val == mid_node or mid_val == mid_node.val)

            mid_val = array[len(array) // 2 + 1] if len(array) >= 3 else None
            mid_node = obj.mid_or_down_mid_next_node(head)
            self.assertTrue(mid_val == mid_node or mid_val == mid_node.val)


if __name__ == "__main__":
    unittest.main()
