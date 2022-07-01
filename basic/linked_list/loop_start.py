#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import unittest
from typing import Optional

from utils import Node, random_linked_list


class LoopStart:

    def solution1(self, head: Node) -> Optional[Node]:
        if not head or not head.next or not head.next.next:
            return

        exists = set()
        while head:
            if head in exists:
                return head
            exists.add(head)
            head = head.next

        return None

    def solution2(self, head: Node) -> Optional[Node]:
        if not head or not head.next or not head.next.next:
            return

        slow, fast = head.next, head.next.next
        while slow != fast:
            if fast.next is None or fast.next.next is None:
                return None
            slow = slow.next
            fast = fast.next.next

        # slow fast 相遇
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = LoopStart()
        for _ in range(10000):
            head = random_linked_list(0, 100, 0, 100)
            # add cercul
            nodes = []
            cur = head
            while cur:
                nodes.append(cur)
                cur = cur.next
            if nodes:
                nodes[-1].next = random.choice(nodes + [None])
            ans1 = obj.solution1(head)
            ans2 = obj.solution2(head)
            self.assertEqual(ans1, ans2)


if __name__ == "__main__":
    unittest.main()
