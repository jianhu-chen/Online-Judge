# coding=utf-8
from typing import List


def bubble_sort(nums: List[int]):
    n = len(nums)
    if n < 2:
        return

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def selection_sort(nums: List[int]):
    n = len(nums)
    if n < 2:
        return

    for i in range(n - 1):
        min_num_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_num_idx]:
                min_num_idx = j

        if i != min_num_idx:
            nums[i], nums[min_num_idx] = nums[min_num_idx], nums[i]


def insertion_sort(nums: List[int]):
    n = len(nums)
    if n < 2:
        return

    for i in range(1, n):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]


def quick_sort(nums: List[int]):
    n = len(nums)
    if n < 2:
        return

    def _sort(nums: List[int], start: int, end: int):
        if start >= end:
            return

        pivot = nums[start]
        left, right = start, end
        while left < right:
            while left < right and nums[right] > pivot:
                right -= 1
            nums[left] = nums[right]

            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]

        nums[left] = pivot
        _sort(nums, start, left - 1)
        _sort(nums, left + 1, end)

    _sort(nums, 0, len(nums) - 1)


def shell_sort(nums: List[int]):
    n = len(nums)
    if n < 2:
        return

    gap = n
    while True:
        gap //= 2
        if gap == 0:
            return
        for i in range(gap, n):
            for j in range(i, 0, -gap):
                if nums[j] < nums[j-gap]:
                    nums[j], nums[j-gap] = nums[j-gap], nums[j]


def merge_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    if n < 2:
        return

    def _merge(left: List[int], right: List[int]):
        i, j = 0, 0
        ret = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ret.append(left[i])
                i += 1
            else:
                ret.append(right[j])
                j += 1

        ret += left[i:]
        ret += right[j:]
        return ret

    def _divide(nums: List[int]):
        if len(nums) < 2:
            return nums

        mid = len(nums) // 2
        left = _divide(nums[:mid])
        right = _divide(nums[mid:])
        return _merge(left, right)

    return _divide(nums)


def heap_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    if n < 2:
        return

    def _heapify(nums: List[int], idx: int, n: int = None):
        c1_idx = 2 * idx + 1
        c2_idx = 2 * idx + 2

        max_idx = idx
        if n is None:
            n = len(nums)
        if c1_idx < n and nums[c1_idx] > nums[max_idx]:
            max_idx = c1_idx
        if c2_idx < n and nums[c2_idx] > nums[max_idx]:
            max_idx = c2_idx

        if max_idx != idx:
            nums[idx], nums[max_idx] = nums[max_idx], nums[idx]
            _heapify(nums, max_idx, n)

    def _build_heap(nums: List[int]):
        n = len(nums)
        latest_node_idx = n - 1
        parent_node_idx = (latest_node_idx - 1) // 2

        for i in range(parent_node_idx, -1, -1):
            _heapify(nums, i)

    _build_heap(nums)
    n = len(nums)
    for i in range(n-1, -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        _heapify(nums, idx=0, n=i)
