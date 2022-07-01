#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from utils import (
    Node,
    DoubleNode,
    random_linked_list,
    linked_list_to_string,
    random_double_linked_list,
    double_linked_list_to_string
)


class ReverseLinkedList:

    def solution(self, head: Node) -> Node:
        if not head or not head.next:
            return head

        prev, next = None, None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev


class ReverseDoubleLinkedList:

    def solution(self, head: DoubleNode) -> DoubleNode:
        if not head or not head.next:
            return head

        prev, next = None, None
        while head:
            next = head.next
            head.next = prev
            head.prev = next
            prev = head
            head = next
        return prev


class Tester(unittest.TestCase):

    def test_reverse_linked_list(self):
        obj = ReverseLinkedList()
        for _ in range(10000):
            head = random_linked_list(min_size=0, max_size=50, min_value=0, max_value=9999)
            array = list(map(
                lambda x: int(x), linked_list_to_string(head, sep=",").split(",")
            )) if head else []
            ans = obj.solution(head)
            ans_array = list(map(
                lambda x: int(x), linked_list_to_string(ans, sep=",").split(",")
            )) if ans else []
            self.assertEqual(array[::-1], ans_array)

    def test_reverse_double_linked_list(self):
        obj = ReverseDoubleLinkedList()
        for _ in range(10000):
            head = random_double_linked_list(min_size=0, max_size=50, min_value=0, max_value=9999)
            array = list(map(
                lambda x: int(x),
                double_linked_list_to_string(head, sep=",").split(",")
            )) if head else []
            ans = obj.solution(head)
            ans_array = list(map(
                lambda x: int(x),
                double_linked_list_to_string(ans, sep=",").split(",")
            )) if ans else []
            self.assertEqual(array[::-1], ans_array)


if __name__ == "__main__":
    head = random_double_linked_list(min_size=0, max_size=10, min_value=0, max_value=9999)
    print(double_linked_list_to_string(head))
    obj = ReverseDoubleLinkedList()
    head = obj.solution(head)
    print(double_linked_list_to_string(head))
    unittest.main()
