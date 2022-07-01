#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest

from utils import Node, random_linked_list, linked_list_to_string


class DeleteGivenValue:
    """
    在链表中删除指定值的所有节点.
    """

    def solution(self, head: Node, value: int) -> Node:
        if not head:
            return

        # 先找到第一个不需要删除的节点
        while head:
            if head.val != value:
                break
            head = head.next

        # pre指向第一个不需要删除的节点
        # cur指向下一个节点
        pre = head
        cur = head.next if head else None
        while cur:
            if cur.val == value:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head


class Tester(unittest.TestCase):

    def test_reverse_linked_list(self):
        obj = DeleteGivenValue()
        for idx, _ in enumerate(range(50000)):
            head = random_linked_list(min_size=0, max_size=100, min_value=0, max_value=100)
            value = random.randint(0, 100)
            array = list(filter(
                lambda x: x != value,
                map(lambda x: int(x), linked_list_to_string(head, sep=",").split(","))
            )) if head else []
            ans = obj.solution(head, value)
            ans_array = list(map(
                lambda x: int(x), linked_list_to_string(ans, sep=",").split(",")
            )) if ans else []
            self.assertEqual(array, ans_array, (value, array, ans_array))
            if (idx + 1) % 5000 == 0:
                print(".", end="", flush=True)


if __name__ == "__main__":
    unittest.main()
