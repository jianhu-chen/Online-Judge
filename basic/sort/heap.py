# -*- coding: utf-8 -*-
from typing import Any, List, Callable


class Heap:
    """
    Heap implementation.

    Parameters
    ----------
    max_size : int
        Maximum size of heap.
    comparator : Callable[[Any, Any], bool]
        Comparator function.

    Attributes
    ----------
    heap : List[Any]
        Heap.
    heap_size : int
        Heap size.
    heap_type : str
        Heap type.
    """

    def __init__(self, max_size: int, comparator: Callable = None) -> None:
        self.max_size = max_size
        self.comparator = comparator if comparator else lambda a, b: a > b
        self.heap: List[Any] = [0] * max_size
        self.heap_size: int = 0

    def build_heap(self, values: List[Any]):
        """Build heap from values."""
        if len(values) > self.max_size:
            raise RuntimeError("Heap size is too small!")

        # deep copy
        for v in values:
            self.heap[self.heap_size] = v
            self.heap_size += 1

        # use heapify to build heap is faster than push all values
        for i in range(len(values) - 1, -1, -1):
            self.heapify(idx=i)

    def push(self, value: Any) -> None:
        """Heap push."""
        if self.full():
            raise RuntimeError("Heap is full!")

        self.heap[self.heap_size] = value
        self.heap_insert(idx=self.heap_size)
        self.heap_size += 1

    def heap_insert(self, idx) -> None:
        """Heap insert from idx."""
        def _parent(idx):
            return (idx - 1) // 2 if idx > 0 else 0

        while self.comparator(self.heap[idx], self.heap[_parent(idx)]):
            # swap with parent
            self.heap[idx], self.heap[_parent(idx)] = self.heap[_parent(idx)], self.heap[idx]
            # update index
            idx = _parent(idx)

    def pop(self) -> Any:
        """Heap pop."""
        if self.empty():
            raise RuntimeError("Heap is empty!")

        ans = self.heap[0]
        # swap with last element
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        # update heap size
        self.heap_size -= 1
        # heapify
        self.heapify(idx=0)
        return ans

    def heapify(self, idx: int) -> None:
        """Heapify from idx."""
        # get left child
        left = 2 * idx + 1
        while left < self.heap_size:  # if left child exists, maybe right child exists
            if left + 1 < self.heap_size and self.comparator(self.heap[left + 1], self.heap[left]):
                largest_idx = left + 1
            else:
                largest_idx = left
            # compare with largest child
            if self.comparator(self.heap[idx], self.heap[largest_idx]):
                break
            # swap with largest child
            self.heap[idx], self.heap[largest_idx] = self.heap[largest_idx], self.heap[idx]
            # update index
            idx = largest_idx
            # get left child
            left = 2 * idx + 1

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

    def full(self) -> bool:
        """Heap full."""
        return self.heap_size == self.max_size
