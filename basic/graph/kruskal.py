#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import heapq
import unittest
from typing import Any, List

from utils import Edge, Graph


class DisjointSet:
    """简化版的并查集."""

    def __init__(self, nodes: List[Any]) -> None:
        node_set = {}
        for node in nodes:
            node_set[node] = set([node])
        self.node_set = node_set

    def is_same_set(self, node1: Any, node2: Any) -> bool:
        return self.node_set[node1] == self.node_set[node2]

    def union(self, node1: Any, node2: Any) -> None:
        set1 = self.node_set[node1]
        set2 = self.node_set[node2]
        for node in set2:
            set1.add(node)
            self.node_set[node] = set1


class KruskalMST:

    def solution(self, graph: Graph) -> List[Edge]:
        disjoint_set = DisjointSet(graph.nodes.values())
        heap = [e for e in graph.edges]
        # TODO: replace to my heap
        heapq.heapify(heap)

        edge_result: List[Edge] = []

        while heapq:
            edge: Edge = heapq.heappop(heap)
            if not disjoint_set.is_same_set(edge.src, edge.des):
                edge_result.append(edge)
                disjoint_set.union(edge.src, edge.des)

        return edge_result


class Tester(unittest.TestCase):

    def test_solution(self):
        # TODO
        pass


if __name__ == "__main__":
    unittest.main()
