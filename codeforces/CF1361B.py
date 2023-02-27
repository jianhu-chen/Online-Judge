#!/usr/bin/env python3
# -*- coding: utf-8 -*-
MOD1 = 10 ** 9 + 7
MOD2 = 10 ** 9 + 3


class Solution:
    """https://codeforces.com/contest/1361/problem/B."""

    def johnnyAndGrandmaster(self, p, kk):
        if p == 1:
            return len(kk) % 2

        kk.sort(reverse=True)
        ans1 = ans2 = 0
        for k in kk:
            if ans1 == 0 and ans2 == 0:
                ans1 = pow(p, k, MOD1)
                ans2 = pow(p, k, MOD2)
            else:
                ans1 = ((ans1 - pow(p, k, MOD1)) % MOD1 + MOD1) % MOD1
                ans2 = ((ans2 - pow(p, k, MOD2)) % MOD2 + MOD2) % MOD2
        return ans1


if __name__ == "__main__":
    for _ in range(int(input())):
        p = int(input().strip().split()[1])
        kk = [int(x) for x in input().strip().split()]
        ans = Solution().johnnyAndGrandmaster(p, kk)
        print(ans)
