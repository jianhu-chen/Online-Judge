#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import Any, List, Callable


class Heap:

    def __init__(self, max_size: int, comparator: Callable = None) -> None:
        self.max_size = max_size
        self.comparator = comparator if comparator else lambda a, b: a > b
        self.heap: List[Any] = [0] * max_size
        self.heap_size: int = 0

    def build_heap(self, values: List[Any]):
        """Build heap from values."""
        if len(values) > self.max_size:
            raise RuntimeError("Heap size is too small!")

        # deep copy
        for v in values:
            self.heap[self.heap_size] = v
            self.heap_size += 1

        # use heapify to build heap is faster than push all values
        for i in range(len(values) - 1, -1, -1):
            self.heapify(idx=i)

    def push(self, value: Any) -> None:
        """Heap push."""
        if self.full():
            raise RuntimeError("Heap is full!")

        self.heap[self.heap_size] = value
        self.heap_insert(idx=self.heap_size)
        self.heap_size += 1

    def heap_insert(self, idx) -> None:
        """Heap insert from idx."""
        def _parent(idx):
            return (idx - 1) // 2 if idx > 0 else 0

        while self.comparator(self.heap[idx], self.heap[_parent(idx)]):
            # swap with parent
            self.heap[idx], self.heap[_parent(idx)] = self.heap[_parent(idx)], self.heap[idx]
            # update index
            idx = _parent(idx)

    def pop(self) -> Any:
        """Heap pop."""
        if self.empty():
            raise RuntimeError("Heap is empty!")

        ans = self.heap[0]
        # swap with last element
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        # update heap size
        self.heap_size -= 1
        # heapify
        self.heapify(idx=0)
        return ans

    def heapify(self, idx: int) -> None:
        """Heapify from idx."""
        # get left child
        left = 2 * idx + 1
        while left < self.heap_size:  # if left child exists, maybe right child exists
            if left + 1 < self.heap_size and self.comparator(self.heap[left + 1], self.heap[left]):
                largest_idx = left + 1
            else:
                largest_idx = left
            # compare with largest child
            if self.comparator(self.heap[idx], self.heap[largest_idx]):
                break
            # swap with largest child
            self.heap[idx], self.heap[largest_idx] = self.heap[largest_idx], self.heap[idx]
            # update index
            idx = largest_idx
            # get left child
            left = 2 * idx + 1

    def top(self) -> Any:
        """Heap top."""
        if self.empty():
            raise RuntimeError("Heap is empty!")
        return self.heap[0]

    def size(self) -> int:
        """Heap size."""
        return self.heap_size

    def empty(self) -> bool:
        """Heap empty."""
        return self.heap_size == 0

    def full(self) -> bool:
        """Heap full."""
        return self.heap_size == self.max_size


class IPO:
    """
    假设公司IPO。为了以更高的价格将股票卖给风险投资公司, 公司希望在 IPO 之前开展一些项目以增加其资本。
    由于资源有限，它只能在 IPO 之前完成最多 k 个不同的项目。帮助公司设计完成最多 k 个不同项目后得到最大总资本的方式。

    给你 n 个项目。对于每个项目 i ，它都有一个纯利润 profits[i] ，和启动该项目需要的最小资本 capital[i] 。

    最初，你的资本为 w 。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。

    总而言之，从给定项目中选择 最多 k 个不同项目的列表，以 最大化最终资本 ，并输出最终可获得的最多资本。

    答案保证在 32 位有符号整数范围内。

    https://leetcode.cn/problems/ipo/
    """

    def solution1(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        def process(pc, w, k):
            """返回可获得的最大资本."""
            if k == 0 or len(pc) == 0:
                return w
            ans = w
            for i in range(len(pc)):
                if pc[i][1] > w:
                    continue
                ans = max(ans, process(pc[:i] + pc[i + 1:], w + pc[i][0], k - 1))
            return ans

        pc = list(zip(profits, capital))
        return process(pc, w, k)

    def solution2(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pc = list(zip(profits, capital))
        capital_heap = Heap(len(pc), lambda x, y: x[1] < y[1])  # 小顶堆
        capital_heap.build_heap(pc)
        profits_heap = Heap(len(pc), lambda x, y: x[0] > y[0])  # 大顶堆
        while k > 0:
            while not capital_heap.empty():
                top = capital_heap.top()
                if top[1] > w:
                    break
                profits_heap.push(capital_heap.pop())
            if profits_heap.empty():
                return w
            else:
                p = profits_heap.pop()
                w += p[0]
                k -= 1
        return w


class Tester(unittest.TestCase):

    def test_solution(self):
        import time
        obj = IPO()
        s1_cost = 0
        s2_cost = 0
        for _ in range(100):
            w = random.randint(1, 100)
            length = random.randint(1, 10)
            k = random.randint(1, length)
            profits = [random.randint(1, 100) for _ in range(length)]
            capital = [random.randint(1, 100) for _ in range(length)]
            s1 = time.perf_counter()
            ans1 = obj.solution1(k, w, profits, capital)
            s1_cost += time.perf_counter() - s1
            s2 = time.perf_counter()
            ans2 = obj.solution2(k, w, profits, capital)
            s2_cost += time.perf_counter() - s2
            self.assertEqual(ans1, ans2, (w, k, profits, capital))
        print(f"solution1 cost: {s1_cost}")
        print(f"solution2 cost: {s2_cost}")


if __name__ == "__main__":
    unittest.main()
