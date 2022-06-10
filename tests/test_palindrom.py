#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import string
import unittest

from basic.palindrome import manacher_str, palindrome_str

TEST_TIMES = 100000  # 10w times test
MIN_LENGTH = 1
MAX_LENGTH = 100000


def random_string(min_length: int = MIN_LENGTH, max_length: int = MAX_LENGTH) -> str:
    return "".join(
        random.choice(string.ascii_letters)
        for _ in range(random.randint(min_length, min_length))
    )


class TestPalindrome(unittest.TestCase):

    def test_manacher_str(self):
        for _ in range(TEST_TIMES):
            s = random_string()
            self.assertEqual(manacher_str(s), palindrome_str(s))


if __name__ == "__main__":
    unittest.main()
