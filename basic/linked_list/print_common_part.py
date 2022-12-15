#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from utils import Node, random_linked_list


class PrintCommonPart:

    def solution1(self, head1: Node, head2: Node) -> list:
        count = {}
        while head1:
            count[head1.val] = count.get(head1.val, 0) + 1
            head1 = head1.next

        answer = []
        while head2:
            if count.get(head2.val, 0) > 0:
                answer.append(head2.val)
                count[head2.val] -= 1
            head2 = head2.next

        return answer

    def solution2(self, head1: Node, head2: Node) -> list:
        """打印两个有序链表的公共部分.

        思路:两个指针, 谁小谁移动, 相等时输出, 直到遇到None
        """
        answer = []
        while head1 and head2:
            if head1.val > head2.val:
                head2 = head2.next
            elif head1.val < head2.val:
                head1 = head1.next
            else:
                answer.append(head1.val)
                head1 = head1.next
                head2 = head2.next
        return answer


class Tester(unittest.TestCase):

    def test_print_common_part(self):
        obj = PrintCommonPart()
        for _ in range(10000):
            head1 = random_linked_list(
                min_size=0, max_size=20, min_value=0, max_value=99, sort=True)
            head2 = random_linked_list(
                min_size=0, max_size=20, min_value=0, max_value=99, sort=True)
            self.assertEqual(
                obj.solution1(head1, head2),
                obj.solution2(head1, head2)
            )


if __name__ == "__main__":
    unittest.main()
