#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from typing import List, Mapping

from utils import Node, Graph


class TopologySort:

    def solution(self, graph: Graph) -> List[Node]:
        # 节点到其入度的映射
        in_map: Mapping[Node: int] = dict()
        # 只有入度为0的节点才能入队列
        zero_in_queue: List[Node] = []

        for node in graph.nodes.values():
            in_map[node] = node.indegree
            if node.indegree == 0:
                zero_in_queue.append(node)

        result: List[Node] = []
        while zero_in_queue:
            cur = zero_in_queue.pop(0)
            result.append(cur)
            for next in cur.nexts:
                in_map[next] -= 1
                if in_map[next] == 0:
                    zero_in_queue.append(next)

        return result


class Tester(unittest.TestCase):

    def test_solution(self):
        # TODO
        pass


if __name__ == "__main__":
    unittest.main()
