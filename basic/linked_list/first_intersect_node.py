#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import Optional

from utils import Node, random_linked_list


class FirstIntersectNode:
    """
    找到两个单链表(可能有环)的第一个相交点并返回, 若没有相交点, 返回None
    """

    def solution(self, head1: Node, head2: Node) -> Optional[Node]:
        """
        case 1: 两个链表都没有环
          case 1.1: 不相交
            1 -> 2 -> 3 -> 4 -> 5 -> 6
            6 -> 7
          case 1.2: 相交
            1 -> 2 -> 3 -> 4 -> 5 -> 6
            6 -> 7 ↗
        case 2: 两个链表有一个有环, 不可能有相交点
        case 3: 两个链表都有环
          case 3.1: 各自成环, 不相交
            1 -> 2 -> 3 -> 4 -> 5 -> 6
                           ↑         ↓
                           ↑ < - < - ↓
            1 -> 2 -> 3 -> 4 -> 5 -> 6
                           ↑         ↓
                           ↑ < - < - ↓
          case 3.2: 入环节点相同
            1 -> 2 -> 3 -> 4 -> 5 -> 6
                    ↗      ↑         ↓
            6 -> 7 ↗       ↑ < - < - ↓
          case 3.3: 入环节点不同
            1 -> 2 -> 3 -> 4
                      ↑    ↓
            9 -> 3 -> 6 <- 5
        """
        if not head1 or not head2:
            return None

        loop1 = self.loop_start(head1)
        loop2 = self.loop_start(head2)

        # case1: 都没有环
        if not loop1 and not loop2:
            diff = 0
            cur1, cur2 = head1, head2
            while cur1.next is not None:
                cur1 = cur1.next
                diff += 1
            while cur2.next is not None:
                cur2 = cur2.next
                diff -= 1
            if cur1 != cur2:  # case 1.1: 两个链表不相交
                return
            # case 1.2: 两个链表相交
            longer = head1 if diff > 0 else head2
            shorter = head1 if longer == head2 else head2
            for _ in range(abs(diff)):
                longer = longer.next
            while longer != shorter:
                longer = longer.next
                shorter = shorter.next
            return longer

        # case 2: 一个有环, 一个没有环, 不可能相交
        if not loop1 or not loop2:
            return

        # case 3: 两个链表都有环
        # case 3.2: 入环节点相同
        if loop1 == loop2:
            diff = 0
            cur1, cur2 = head1, head2
            while cur1.next != loop1:
                cur1 = cur1.next
                diff += 1
            while cur2.next != loop2:
                cur2 = cur2.next
                diff -= 1
            longer = head1 if diff > 0 else head2
            shorter = head1 if longer == head2 else head2
            while longer != shorter:
                longer = longer.next
                shorter = shorter.next
            return longer

        cur = loop1
        while cur.next != loop1:
            cur = cur.next
            # case 3.3: 入环节点不同
            if cur == loop2:
                return loop1

        # case 3.1: 各自成环, 不相交
        return None

    @staticmethod
    def loop_start(head):
        if not head or not head.next or not head.next.next:
            return
        slow, fast = head.next, head.next.next
        while slow != fast:
            if not fast.next or not fast.next.next:
                return
            slow, fast = slow.next, fast.next.next
        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow


class Tester(unittest.TestCase):

    obj = FirstIntersectNode()

    def test_case1(self):
        inter_cnt = 0
        for _ in range(10000):
            head1 = random_linked_list(0, 100, 0, 100)
            head2 = random_linked_list(0, 100, 0, 100)
            gt = None
            if head1:
                tail1 = head1
                while tail1.next:
                    tail1 = tail1.next
                inter = random.randint(0, 85)
                tail2 = head2
                while tail2 and inter > 0:
                    tail2 = tail2.next
                    inter -= 1
                if tail2:
                    tail1.next = tail2
                    gt = tail2

            if gt is not None:
                inter_cnt += 1

            if random.random() < 0.5:
                head1, head2 = head2, head1

            ans = self.obj.solution(head1, head2)
            self.assertEqual(ans, gt)
        inter_rate = inter_cnt / (10000)
        print("Test case 1.1: {:.2%}, 1.2: {:.2%}".format(1 - inter_rate, inter_rate))

    def test_case2(self):
        one_loop_cnt = 0
        for _ in range(10000):
            head1 = random_linked_list(0, 100, 0, 100)
            head2 = random_linked_list(0, 100, 0, 100)
            if head1:
                tail1 = head1
                while tail1.next:
                    tail1 = tail1.next
                loop_n = random.randint(0, 50)
                cur = head1
                while cur and loop_n > 0:
                    cur = cur.next
                    loop_n -= 1
                if cur:
                    tail1.next = cur
                    one_loop_cnt += 1

            if random.random() < 0.5:
                head1, head2 = head2, head1

            ans = self.obj.solution(head1, head2)
            self.assertEqual(ans, None)
        one_loop_rate = one_loop_cnt / 10000
        print("Test case 2.1: {:.2%}".format(one_loop_rate))

    def test_case3_1(self):
        both_loop_cnt = 0
        for _ in range(10000):
            head1 = random_linked_list(0, 100, 0, 100)
            head2 = random_linked_list(0, 100, 0, 100)
            both_loop = True
            for head in (head1, head2):
                if head:
                    tail = head
                    while tail.next:
                        tail = tail.next
                    loop_n = random.randint(0, 20)
                    cur = head
                    while cur and loop_n > 0:
                        cur = cur.next
                        loop_n -= 1
                    if cur:
                        tail.next = cur
                    else:
                        both_loop = False

            if both_loop:
                both_loop_cnt += 1

            if random.random() < 0.5:
                head1, head2 = head2, head1

            ans = self.obj.solution(head1, head2)
            self.assertEqual(ans, None)
        print("Test case 3.1: {:.2%}".format(both_loop_cnt / 10000))

    def test_case3_2(self):
        pass

    def test_case3_3(self):
        pass


if __name__ == "__main__":
    unittest.main()
