#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import List

from utils import Node, copy_linked_list, random_linked_list


class NetherlandsFlag:
    """
    荷兰国旗问题 (链表版).
    """

    def solution1(self, head: Node, num: int) -> Node:
        if not head:
            return head

        array: List[Node] = []
        while head:
            array.append(head)
            head = head.next

        left, right = -1, len(array)
        idx = 0
        while idx < right:
            if array[idx].val < num:
                left += 1
                array[left], array[idx] = array[idx], array[left]
                idx += 1
            elif array[idx].val > num:
                right -= 1
                array[right], array[idx] = array[idx], array[right]
            else:
                idx += 1

        for idx in range(len(array) - 1):
            array[idx].next = array[idx + 1]
        array[-1].next = None

        return array[0]

    def solution2(self, head: Node, num: int) -> Node:
        lh, lt = None, None  # 小于区域头尾结点
        eh, et = None, None  # 等于区域头尾结点
        gh, gt = None, None  # 大于区域头尾结点

        while head:
            if head.val < num:
                if lh is None:
                    lh = head
                    lt = head
                else:
                    lt.next = head
                    lt = head
            elif head.val == num:
                if eh is None:
                    eh = head
                    et = head
                else:
                    et.next = head
                    et = head
            else:
                if gh is None:
                    gh = head
                    gt = head
                else:
                    gt.next = head
                    gt = head
            head = head.next

        tmp = Node(0)
        ans = tmp
        # 将6个指针串联起来
        for h, t in ((lh, lt), (eh, et), (gh, gt)):
            if h is not None:
                tmp.next = h
                tmp = t
        tmp.next = None
        return ans.next


class Tester(unittest.TestCase):

    def test_netherlands_flag(self):
        obj = NetherlandsFlag()
        for _ in range(10000):
            head1 = random_linked_list(min_size=0, max_size=50, min_value=0, max_value=100)
            head2 = copy_linked_list(head1)
            num = random.randint(0, 10)

            # test solution1
            ans1 = obj.solution1(head1, num)
            check_equal_flag = False
            check_grater_flag = False
            while ans1:
                if ans1.val == num:
                    check_equal_flag = True
                if ans1.val > num:
                    check_grater_flag = True
                if check_equal_flag:
                    self.assertGreaterEqual(ans1.val, num)
                if check_grater_flag:
                    self.assertGreater(ans1.val, num)
                ans1 = ans1.next

            # test solution2
            ans2 = obj.solution2(head2, num)
            check_equal_flag = False
            check_grater_flag = False
            while ans2:
                if ans2.val == num:
                    check_equal_flag = True
                if ans2.val > num:
                    check_grater_flag = True
                if check_equal_flag:
                    self.assertGreaterEqual(ans2.val, num)
                if check_grater_flag:
                    self.assertGreater(ans2.val, num)
                ans2 = ans2.next


if __name__ == "__main__":
    unittest.main()
