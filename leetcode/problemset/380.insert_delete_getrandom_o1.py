#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/insert-delete-getrandom-o1
import random


class RandomizedSet:

    def __init__(self):
        self.idx2val = {}
        self.val2idx = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.val2idx:
            return False

        self.val2idx[val] = self.size
        self.idx2val[self.size] = val
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val2idx:
            return False

        idx = self.val2idx.pop(val)
        if idx == self.size - 1:
            self.idx2val.pop(idx)
            self.size -= 1
            return True

        last_val = self.idx2val[self.size - 1]
        self.idx2val[idx] = last_val
        self.val2idx[last_val] = idx
        self.size -= 1
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, self.size - 1)
        return self.idx2val[idx]
