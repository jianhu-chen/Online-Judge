# -*- coding: utf-8 -*-


class TextEditor:

    def __init__(self):
        self.str = ""
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.str = self.str[:self.cursor] + text + self.str[self.cursor:]
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        k = min(k, self.cursor)
        self.str = self.str[:self.cursor - k] + self.str[self.cursor:]
        self.cursor -= k
        return k

    def cursorLeft(self, k: int) -> str:
        k = min(k, self.cursor)
        self.cursor -= k
        return self.str[max(0, self.cursor - 10):self.cursor]

    def cursorRight(self, k: int) -> str:
        num_rights = len(self.str) - self.cursor
        k = min(num_rights, k)
        self.cursor += k
        return self.str[max(0, self.cursor - 10):self.cursor]
