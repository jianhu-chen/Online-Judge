# -*- coding: utf-8 -*-

def swap(num1, num2):
    """
    不使用任何额外的变量, 交换两个数字的值.
    """
    num1 ^= num2
    num2 ^= num1
    num1 ^= num2
    return num1, num2


def one_number_odd_times(array):
    """
    一个数组中只有一种数出现了奇数次, 其他数都出现了偶数次, 找到这个数并返回.
    """
    eor = 0
    for num in array:
        eor ^= num
    return eor


def two_number_odd_times(array):
    """
    一个数组中有两种数出现了奇数次, 其他数都出现了偶数次, 找到这两个数并返回(升序).
    """
    eor = 0
    for num in array:
        eor ^= num

    # 提取最右侧的1
    right_one = eor & (~eor + 1)
    num1 = 0
    for num in array:
        if right_one & num:
            num1 ^= num

    num2 = eor ^ num1
    return sorted([num1, num2])
