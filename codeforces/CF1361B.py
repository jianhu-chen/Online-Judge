#!/usr/bin/env python3
# -*- coding: utf-8 -*-
MOD = 10 ** 9 + 7


class Solution:
    """https://codeforces.com/problemset/problem/1361/B."""

    def johnnyAndGrandmaster(self, p, ks):
        if p == 1:
            return len(ks) % 2

        ks.sort(reverse=True)
        ans = 0
        for k in ks:
            if ans == 0:
                ans = pow(p, k, MOD)
            else:
                ans -= pow(p, k, MOD)
        return ans


if __name__ == "__main__":
    for _ in range(int(input())):
        p = int(input().strip().split()[1])
        ks = [int(x) for x in input().strip().split()]
        ans = Solution().johnnyAndGrandmaster(p, ks)
        print(ans)
