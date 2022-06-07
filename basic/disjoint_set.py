# -*- coding: utf-8 -*-
from typing import Any, List


class DisjointSet:

    def __init__(self, nodes: List[Any]) -> None:
        self.parent = {n: n for n in nodes}
        self.rank = {n: 1 for n in nodes}

    def _find(self, node: Any) -> Any:
        path = []
        while self.parent[node] != node:
            path.append(node)
            node = self.parent[node]
        # flatten
        while len(path) != 0:
            self.parent[path.pop()] = node
        return node

    def is_same(self, node1: Any, node2: Any) -> bool:
        return self._find(node1) == self._find(node2)

    def union(self, node1: Any, node2: Any) -> None:
        h1 = self._find(node1)
        h2 = self._find(node2)
        if h1 == h2:
            return

        big = h1 if self.rank[h1] > self.rank[h2] else h2
        small = h1 if big == h2 else h2

        self.parent[small] = big
        self.rank[big] += self.rank[small]
        self.rank.pop(small)

    def size(self) -> int:
        return len(self.rank)
