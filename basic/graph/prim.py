#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import heapq
import unittest
from typing import Set, List

from utils import Edge, Node, Graph


class PrimMST:

    def solution(self, graph: Graph) -> List[Edge]:
        # 小根堆维护边的权重
        heap = [e for e in graph.edges]
        heapq.heapify(heap)

        visit: Set[Node] = set()
        edge_result: Set[Edge] = set()

        for node in graph.nodes.values():  # 可能存在森林问题
            if node not in visit:
                visit.add(node)
                for edge in node.edges:
                    heapq.heappush(heap, edge)
                while heap:
                    # 权重最小的边
                    edge: Edge = heapq.heappop(heap)
                    # 还没访问过, 加入
                    if edge.des not in visit:
                        visit.add(edge.des)
                        edge_result.add(edge)
                        for edge_next in edge.des.edges:
                            heapq.heappush(heap, edge_next)

        return edge_result


class Tester(unittest.TestCase):

    def test_solution(self):
        # TODO
        pass


if __name__ == "__main__":
    unittest.main()
