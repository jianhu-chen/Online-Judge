# -*- coding: utf-8 -*-
from typing import List


class TrieNode:

    def __init__(self):
        self.p = 0
        self.e = 0
        self.nexts = [None] * 26

    def __repr__(self):
        return "Node(p={}, e={})".format(self.p, self.e)

    __str__ = __repr__


class Trie:

    def __init__(self, words: List[str]) -> None:
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word: str):
        """Insert a word into the trie."""
        if not word:
            return

        chs = list(word)
        node = self.root
        node.p += 1
        for ch in chs:
            index = ord(ch) - ord('a')
            if node.nexts[index] is None:
                node.nexts[index] = TrieNode()
            node = node.nexts[index]
            node.p += 1
        node.e += 1

    def search(self, word: str) -> int:
        """Return the number of times the word is in the trie."""
        if not word:
            return False

        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if node.nexts[index] is None:
                return False
            node = node.nexts[index]
        return node.e

    def prefix(self, pre: str) -> int:
        """Return the number of words with the prefix."""
        if not pre:
            return 0

        node = self.root
        for ch in pre:
            index = ord(ch) - ord('a')
            if node.nexts[index] is None:
                return 0
            node = node.nexts[index]
        return node.p

    def delete(self, word: str):
        """Delete the word from the trie."""
        if self.search(word):
            node = self.root
            for ch in word:
                index = ord(ch) - ord('a')
                node.nexts[index].p -= 1
                if node.nexts[index].p == 0:
                    node.nexts[index] = None
                    return
                node = node.nexts[index]
            node.e -= 1
