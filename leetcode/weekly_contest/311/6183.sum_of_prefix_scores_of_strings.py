#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/sum-of-prefix-scores-of-strings
from typing import List


class TrieNode:

    def __init__(self):
        self.p = 0
        self.ends = []
        self.nexts = [None] * 26


class Trie:

    def __init__(self, words: List[str]) -> None:
        self.root = TrieNode()
        for i, word in enumerate(words):
            self.insert(word, i)

    def insert(self, word: str, i: int):
        """Insert a word into the trie."""
        if not word:
            return

        node = self.root
        for ch in list(word):
            index = ord(ch) - ord('a')
            if node.nexts[index] is None:
                node.nexts[index] = TrieNode()
            node = node.nexts[index]
            node.p += 1
        node.ends.append(i)


class Solution:

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie(words)
        scores = [0] * len(words)

        def dfs(node, score):
            score += node.p
            for i in node.ends:
                scores[i] = score
            for child in node.nexts:
                if child:
                    dfs(child, score)

        dfs(trie.root, 0)
        return scores
