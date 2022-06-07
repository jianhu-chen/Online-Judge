# -*- coding: utf-8 -*-

def get_index_of(str1: str, str2: str) -> int:
    """
    在str1中查找str2的位置, 如果找不到返回-1.
    """
    if len(str2) == 0 or len(str1) < len(str2):
        return -1

    # next
    next = [-1 for _ in str2]
    if len(str2) > 1:
        next[1] = 0
        i = 2  # 目前在哪个位置上求next数组的值
        cn = 0  # 当前是哪个位置的值在和i-1位置的字符比较
        while i < len(str2):
            if str2[i - 1] == str2[cn]:
                next[i] = cn + 1
                i += 1
                cn += 1
            elif cn != -1:
                cn = next[cn]
            else:
                next[i] = 0
                i += 1

    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        elif next[j] != -1:
            j = next[j]
        else:
            i += 1

    return i - j if j == len(str2) else -1
