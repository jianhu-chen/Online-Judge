#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import unittest
from typing import Set, List

from utils import Node, random_graph


class DFS:

    def solution(self, node: Node) -> List[Node]:
        if not node:
            return []

        result: List[Node] = [node]
        stack: List[Node] = [node]
        visit: Set[Node] = set([node])
        while stack:
            cur = stack.pop()
            for next in cur.nexts:
                if next not in visit:
                    stack.append(cur)
                    stack.append(next)
                    result.append(next)
                    visit.add(next)
                    break
        return result


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = DFS()
        graph = random_graph(1, 7)
        print(graph)
        node = random.choice(graph.nodes)
        ans = obj.solution(node)
        print(ans)


if __name__ == "__main__":
    unittest.main()
