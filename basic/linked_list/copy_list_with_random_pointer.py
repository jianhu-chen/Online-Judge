#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest

from utils import random_array


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None  # only difference from Node


class CopyListWithRandomPointer:
    """
    复制含有随机指针的单链表.

    ref: https://leetcode.cn/problems/copy-list-with-random-pointer/
    """

    def solution1(self, head: Node) -> Node:
        if not head:
            return

        mapper = {}  # map old node to new node
        cur = head
        while cur:
            mapper[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            mapper[cur].next = mapper[cur.next] if cur.next else None
            mapper[cur].random = mapper[cur.random] if cur.random else None
            cur = cur.next

        return mapper[head]

    def solution2(self, head: Node) -> Node:
        if not head:
            return

        # 1 -> 2 -> 3 -> null => 1 -> 1' -> 2 -> 2' -> 3 -> 3' -> null
        cur = head
        while cur:
            new = Node(cur.val)
            new.next = cur.next
            cur.next = new
            cur = new.next

        cur = head
        while cur:
            if cur.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 分离
        cur = head
        ans = head.next
        ans_cur = ans
        while cur:
            cur.next = cur.next.next
            cur = cur.next
            ans_cur.next = cur.next if cur is not None else None
            ans_cur = ans_cur.next

        return ans


def random_linked_list() -> Node:
    array = random_array(0, 100, 0, 100)
    if not array:
        return None

    head = Node(array[0])
    tail = head
    node_array = [head]
    for i in range(1, len(array)):
        tail.next = Node(array[i])
        tail = tail.next
        node_array.append(tail)

    for node in node_array:
        node.random = random.choice(node_array + [None])

    return head


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = CopyListWithRandomPointer()
        for _ in range(10000):
            head = random_linked_list()
            ans1 = obj.solution1(head)
            ans2 = obj.solution2(head)
            while head and ans1 and ans2:
                self.assertEqual(head.val, ans1.val)
                self.assertEqual(head.val, ans2.val)
                if head.random is not None:
                    self.assertEqual(head.random.val, ans1.random.val)
                    self.assertEqual(head.random.val, ans2.random.val)
                else:
                    self.assertEqual(ans1.random, None)
                    self.assertEqual(ans2.random, None)
                head = head.next
                ans1 = ans1.next
                ans2 = ans2.next
            self.assertEqual(head, ans1)
            self.assertEqual(head, ans2)


if __name__ == "__main__":
    unittest.main()
