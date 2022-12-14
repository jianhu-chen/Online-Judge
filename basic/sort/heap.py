# -*- coding: utf-8 -*-
import unittest
from typing import Any, List, Callable, Iterable


class Heap:
    """
    Heap implementation.

    Parameters
    ----------
    comparator : Callable[[Any, Any], bool]
        Comparator function.
    """

    def __init__(self, comparator: Callable = None) -> None:
        self.comparator = comparator if comparator else lambda a, b: a > b
        self.heap: List[Any] = []
        self.heap_size: int = 0

    @classmethod
    def from_list(cls, values: Iterable[Any], inplace: bool = False, comparator: Callable = None):
        """Build heap from list."""
        instance = cls(comparator)

        if inplace:
            instance.heap = values
        else:
            instance.heap = [*values]
        instance.heap_size = len(values)

        # use heapify to build heap is faster than push all values
        for i in reversed(range(len(values) // 2)):
            instance.heapify(idx=i)

        return instance

    def heap_insert(self, idx) -> None:
        """Heap insert from idx."""
        def _parent(idx):
            return (idx - 1) // 2 if idx > 0 else 0

        while self.comparator(self.heap[idx], self.heap[_parent(idx)]):
            # swap with parent
            self.heap[idx], self.heap[_parent(idx)] = self.heap[_parent(idx)], self.heap[idx]
            # update index
            idx = _parent(idx)

    def heapify(self, idx: int) -> None:
        """Heapify from idx."""
        # get left child
        left = 2 * idx + 1
        # if left child exists, maybe right child exists
        while left < self.heap_size:
            if left + 1 < self.heap_size and self.comparator(self.heap[left + 1], self.heap[left]):
                largest_idx = left + 1
            else:
                largest_idx = left
            # compare with the largest child
            if self.comparator(self.heap[idx], self.heap[largest_idx]):
                break
            # swap with the largest child
            self.heap[idx], self.heap[largest_idx] = self.heap[largest_idx], self.heap[idx]
            # update index
            idx = largest_idx
            # get left child
            left = 2 * idx + 1

    def push(self, value: Any) -> None:
        """Heap push."""
        self.heap[self.heap_size] = value
        self.heap_insert(idx=self.heap_size)
        self.heap_size += 1

    def pop(self) -> Any:
        """Heap pop."""
        if self.empty():
            raise RuntimeError("Heap is empty!")

        ans = self.heap[0]
        # swap with the last element
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        # update heap size
        self.heap_size -= 1
        # heapify
        self.heapify(idx=0)
        return ans

    def top(self) -> Any:
        """Heap top."""
        if self.empty():
            raise RuntimeError("Heap is empty!")
        return self.heap[0]

    def size(self) -> int:
        """Heap size."""
        return self.heap_size

    def empty(self) -> bool:
        """Heap empty."""
        return self.heap_size == 0

    def clear(self) -> bool:
        """Clean up useless data."""
        del self.heap[self.heap_size:]


class TestHeap(unittest.TestCase):

    def test_from_list(self):
        heap = Heap.from_list([4, 1, 5, 3, 9], )
        self.assertEqual(heap.size(), 5)
        self.assertEqual(heap.heap, [9, 4, 5, 3, 1])
        heap = Heap.from_list([4, 1, 5, 3, 9], comparator=lambda a, b: a < b)
        self.assertEqual(heap.size(), 5)
        self.assertEqual(heap.heap, [1, 3, 5, 4, 9])


if __name__ == "__main__":
    unittest.main()
