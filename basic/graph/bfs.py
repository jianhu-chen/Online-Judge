#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import unittest
from typing import Set, List

from utils import Node, random_graph


class BFS:

    def solution(self, node: Node) -> List[Node]:
        if not node:
            return []

        result = []
        queue: List[Node] = [node]
        visit: Set[Node] = set([node])
        while queue:
            cur = queue.pop(0)
            result.append(cur)
            for next in cur.edges:
                if next.des not in visit:
                    queue.append(next.des)
                    visit.add(next.des)
        return result


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = BFS()
        graph = random_graph(500, 1000)
        node = random.choice(graph.nodes)
        ans = obj.solution(node)
        for i in range(1, len(ans)):
            self.assertIn(ans[i], ans[i - 1].nexts)


if __name__ == "__main__":
    unittest.main()
