# -*- coding: utf-8 -*-
from typing import List


class TrieNode:

    def __init__(self):
        self.p = 0
        self.e = 0
        self.nexts = {}

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
            if node.nexts.get(ch) is None:
                node.nexts[ch] = TrieNode()
            node = node.nexts[ch]
            node.p += 1
        node.e += 1

    def search(self, word: str) -> int:
        """Return the number of times the word is in the trie."""
        if not word:
            return False

        node = self.root
        for ch in word:
            if node.nexts.get(ch) is None:
                return False
            node = node.nexts[ch]
        return node.e

    def prefix(self, pre: str) -> int:
        """Return the number of words with the prefix."""
        if not pre:
            return 0

        node = self.root
        for ch in pre:
            if node.nexts.get(ch) is None:
                return 0
            node = node.nexts[ch]
        return node.p

    def delete(self, word: str):
        """Delete the word from the trie."""
        if self.search(word):
            node = self.root
            for ch in word:
                node.nexts[ch].p -= 1
                if node.nexts[ch].p == 0:
                    node.nexts[ch] = None
                    return
                node = node.nexts[ch]
            node.e -= 1


if __name__ == "__main__":
    Trie(["hello","world!"])