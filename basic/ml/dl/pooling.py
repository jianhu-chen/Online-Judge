#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest


def max_pool1d(x, k=3, s=1, p=0):
    assert len(x) >= k and k > 1
    assert 0 <= p <= k // 2

    q, result = [], []
    for i in range(len(x)):
        if q and q[0] == i - k:
            q.pop(0)
        while q and x[i] > q[-1]:
            q.pop()
        q.append(i)
        if i >= k - 1 and (i - k + 1) % s == 0:
            result.append(x[q[0]])
    return result


class Tester(unittest.TestCase):

    def test_max_pool1d(self):
        self.assertEqual(
            max_pool1d([1, 3, 5, 2, 5, 7, 10, -2], k=2),
            [3, 5, 5, 5, 7, 10, 10]
        )
        self.assertEqual(
            max_pool1d([1, 3, 5, 2, 5, 7, 10, -2], k=3),
            [5, 5, 5, 7, 10, 10]
        )
        self.assertEqual(
            max_pool1d([1, 3, 5, 2, 5, 7, 10, -2], k=2, s=2),
            [3, 5, 7, 10]
        )
        self.assertEqual(
            max_pool1d([1, 3, 5, 2, 5, 7, 10, -2], k=3, s=2),
            [5, 5, 10]
        )


if __name__ == "__main__":
    unittest.main()
