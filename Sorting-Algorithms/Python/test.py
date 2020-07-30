# coding=utf-8
import random
import time
import sort as S

from termcolor import colored


def check(nums):
    if len(nums) < 2:
        return True

    first = True
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            continue
        else:
            if first:
                order = nums[i] > nums[i + 1]
                first = False
            else:
                if nums[i] > nums[i + 1] != order:
                    return False
    return True


def test(nums=None):
    if not nums:
        nums = [random.randint(0, 100) for _ in range(10)]

    algorithms = [ag for ag in dir(S) if ag.endswith("_sort")]
    print(f"Algorithms: {algorithms}\n")
    print(f"Test data: {nums}\n")

    for ag in algorithms:
        nums_copy = nums.copy()
        print("-"*15 + f" {ag} " + "-"*15)
        start = time.time()
        ret = getattr(S, ag)(nums_copy)
        if ret is not None:
            nums_copy = ret
        print(f"After: {nums_copy}")
        ret = check(nums_copy)
        color = "green" if ret else "red"
        print(colored(f"Result: {ret}", color))
        print("-"*15 + f" Time:{time.time() - start} " + "-"*15)
        print("")


if __name__ == "__main__":
    test()
