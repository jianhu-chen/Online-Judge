#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from typing import Any, List


class DisjointSet:
    """Disjoint set with path compression and union by rank."""

    def __init__(self, nodes: List[Any]) -> None:
        self.parent = {n: n for n in nodes}
        self.rank = {n: 1 for n in nodes}

    def is_same_set(self, node1: Any, node2: Any) -> bool:
        """Check if two nodes are in the same set."""
        return self.find(node1) == self.find(node2)

    def find(self, node: Any) -> Any:
        """Find the head of the given node."""
        if node not in self.parent:
            raise ValueError("node not in disjoint set!")

        path = []
        while self.parent[node] != node:
            path.append(node)
            node = self.parent[node]
        # flatten
        while len(path) != 0:
            self.parent[path.pop()] = node
        return node

    def union(self, node1: Any, node2: Any) -> None:
        """Union two disjoint sets."""
        h1 = self.find(node1)
        h2 = self.find(node2)
        if h1 == h2:
            return

        big = h1 if self.rank[h1] > self.rank[h2] else h2
        small = h1 if big == h2 else h2

        self.parent[small] = big
        self.rank[big] += self.rank[small]
        self.rank.pop(small)

    def size(self) -> int:
        """Return the number of disjoint sets."""
        return len(self.rank)


class Tester(unittest.TestCase):

    def test_disjoint_set(self):
        disjoint_set = DisjointSet([1, 2, 3, 4, 5, 6])
        disjoint_set.union(1, 2)
        disjoint_set.union(2, 3)
        disjoint_set.union(4, 5)
        self.assertEqual(disjoint_set.size(), 3)
        self.assertTrue(disjoint_set.is_same_set(1, 3))
        self.assertFalse(disjoint_set.is_same_set(1, 4))

        disjoint_set.union(1, 5)
        self.assertEqual(disjoint_set.size(), 2)
        self.assertTrue(disjoint_set.is_same_set(1, 5))
        self.assertFalse(disjoint_set.is_same_set(1, 6))

        disjoint_set.union(1, 6)
        self.assertEqual(disjoint_set.size(), 1)
        self.assertTrue(disjoint_set.is_same_set(2, 6))


if __name__ == "__main__":
    unittest.main()
