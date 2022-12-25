#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class BloomFilter:

    def __init__(self, m: int, k: int) -> None:
        self.m = m  # size of bitmap
        self.k = k  # num of hash func
        self.bitmap = 0

    def hash_k_times(self, val: str):
        assert isinstance(val, str)
        result = []
        for i in range(self.k):
            result.append(hash(val + str(i)))
        return result

    def set_bit(self, i):
        self.bitmap |= (1 << (i % self.m))

    def get_bit(self, i):
        return (self.bitmap >> (i % self.m)) & 1

    def __contains__(self, val):
        hs = self.hash_k_times(val)
        for h in hs:
            if not self.get_bit(h):
                return False
        return True

    def add(self, val):
        hs = self.hash_k_times(val)
        for h in hs:
            self.set_bit(h)


if __name__ == "__main__":
    b = BloomFilter(m=120, k=8)
    b.add("aa")
    b.add("bb")
    print("aa" in b)
    print("bb" in b)
    print("cc" in b)
