#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import unittest
from typing import Any, Set, List, Mapping

from utils import Edge, Node, random_graph


class Heap:

    def __init__(self, max_size: int) -> None:
        self.max_size = max_size
        self.comparator = lambda a, b: self.distance[a] < self.distance[b]
        self.heap: List[Any] = [0] * max_size
        self.heap_size: int = 0
        # !NOTE: customed
        self.node2idx: Mapping[Node, int] = {}
        self.distance: Mapping[Node, int] = {}  # 源节点出发到该节点的最小距离

    def push(self, value: Any) -> None:
        """Heap push."""
        if self.full():
            raise RuntimeError("Heap is full!")

        # !NOTE: customed
        node, dist = value
        if node not in self.distance:
            # add
            self.heap[self.heap_size] = node
            self.node2idx[node] = self.heap_size
            self.distance[node] = dist
            self.heap_insert(idx=self.heap_size)
            self.heap_size += 1
        elif dist < self.distance[node]:
            # update
            self.distance[node] = dist
            self.heap[self.node2idx[node]] = node
            self.heap_insert(idx=self.node2idx[node])
        else:
            # ignore
            pass

    def heap_insert(self, idx) -> None:
        """Heap insert from idx."""
        def _parent(idx):
            return (idx - 1) // 2 if idx > 0 else 0

        while self.comparator(self.heap[idx], self.heap[_parent(idx)]):
            # swap with parent
            self.heap[idx], self.heap[_parent(idx)] = self.heap[_parent(idx)], self.heap[idx]
            # !NOTE: customed
            self.node2idx[self.heap[idx]] = idx
            self.node2idx[self.heap[_parent(idx)]] = _parent(idx)
            # update index
            idx = _parent(idx)

    def pop(self) -> Any:
        """Heap pop."""
        if self.empty():
            raise RuntimeError("Heap is empty!")

        ans = self.heap[0]
        dist = self.distance[ans]
        # swap with last element
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        # !NOTE: customed
        self.node2idx[self.heap[0]] = 0
        self.node2idx.pop(ans)
        # self.distance.pop(ans)
        # update heap size
        self.heap_size -= 1
        # heapify
        self.heapify(idx=0)
        return ans, dist

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
            # !NOTE: customed
            self.node2idx[self.heap[idx]] = idx
            self.node2idx[self.heap[largest_idx]] = largest_idx
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


class Dijkstra:

    def solution1(self, src: Node) -> List[Edge]:

        def get_min_distance_node(distance: Mapping[Node, int], locked: Set[Node]) -> Node:
            # TODO 可以通过改写堆结构来优化此过程.
            min_node = None
            min_dist = float("inf")
            for node, dist in distance.items():
                if dist < min_dist and node not in locked:
                    min_node = node
                    min_dist = dist
            return min_node

        # distance to src node
        distance = {src: 0}
        # locked nodes
        locked = set()

        min_node = get_min_distance_node(distance, locked)
        while min_node:
            cur_dist = distance[min_node]
            for edge in min_node.edges:
                des = edge.des
                distance[des] = min(distance.get(des, float("inf")), cur_dist + edge.weight)
            locked.add(min_node)
            min_node = get_min_distance_node(distance, locked)

        return distance

    def solution2(self, src: Node) -> List[Edge]:
        # distance to src node
        distance = {src: 0}
        heap = Heap(max_size=1000)
        heap.push((src, 0))

        while not heap.empty():
            cur_node, cur_dist = heap.pop()
            for edge in cur_node.edges:
                heap.push((edge.des, cur_dist + edge.weight))  # add or update or ignore
            distance[cur_node] = cur_dist

        return distance


class Tester(unittest.TestCase):

    def test_solution(self):
        import time
        obj = Dijkstra()
        ans1_cost = 0
        ans2_cost = 0
        test_times = 10
        for _ in range(test_times):
            graph = random_graph(800, 1000)
            src = random.choice(list(graph.nodes.values()))
            s = time.perf_counter()
            ans1 = obj.solution1(src)
            ans1_cost += time.perf_counter() - s
            s = time.perf_counter()
            ans2 = obj.solution2(src)
            ans2_cost += time.perf_counter() - s
            self.assertEqual(len(ans1), len(ans2))
            for node, dist in ans1.items():
                self.assertEqual(dist, ans2[node])
        print("ans1 cost:", ans1_cost)
        print("ans2 cost:", ans2_cost)


if __name__ == "__main__":
    unittest.main()
