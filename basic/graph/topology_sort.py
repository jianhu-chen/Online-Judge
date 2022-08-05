#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from typing import List, Mapping

from utils import Edge, Node, Graph


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
        obj = TopologySort()
        nodes = {i: Node(i) for i in range(8)}
        # 0 -> 7 -> 1 -> 3 -> 4 -> 5
        #       ↘-> 2 ↗   ↘ 6 ↑
        nodes[0].nexts = [nodes[7]]
        nodes[7].nexts = [nodes[1], nodes[2]]
        nodes[1].nexts = [nodes[3]]
        nodes[2].nexts = [nodes[3]]
        nodes[3].nexts = [nodes[4], nodes[6]]
        nodes[6].nexts = [nodes[4]]
        nodes[4].nexts = [nodes[5]]
        edges = set((
            Edge(1, nodes[0], nodes[7]),
            Edge(1, nodes[7], nodes[1]),
            Edge(1, nodes[7], nodes[2]),
            Edge(1, nodes[1], nodes[3]),
            Edge(1, nodes[2], nodes[3]),
            Edge(1, nodes[3], nodes[4]),
            Edge(1, nodes[3], nodes[6]),
            Edge(1, nodes[6], nodes[4]),
            Edge(1, nodes[4], nodes[5]),
        ))
        graph = Graph(nodes, edges)
        ans = obj.solution(graph)
        print(ans)


if __name__ == "__main__":
    unittest.main()
