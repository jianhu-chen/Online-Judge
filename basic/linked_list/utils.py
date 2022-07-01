# -*- coding: utf-8 -*-
import random


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "Node(val={})".format(self.val)

    __str__ = __repr__


class DoubleNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return "DoubleNode(val={})".format(self.val)

    __str__ = __repr__


def random_array(
    min_size: int,
    max_size: int,
    min_value: int,
    max_value: int,
    remove_duplicate: bool = False
) -> list:
    """
    Parameters
    ----------
    min_size : int
        The minimum size of the linked list.
    max_size : int
        The maximum size of the linked list.
    min_value : int
        The minimum value of the linked list.
    max_value : int
        The maximum value of the linked list.
    remove_duplicate : bool
        Whether to remove duplicate elements.

    Returns
    -------
    Node
        The head of the linked list.
    """
    assert min_size >= 0 and max_size >= 1 and min_value <= max_value

    def _generate():
        size = random.randint(min_size, max_size)
        # range: [min_value, max_value]
        array = [random.randint(min_value, max_value) for _ in range(size)]
        if remove_duplicate:
            array = list(set(array))
        random.shuffle(array)
        return array

    array = _generate()
    while len(array) < min_size:
        array = _generate()

    return array


def array_to_linked_list(array: list) -> Node:
    if not array:
        return None

    head = Node(array[0])
    tail = head
    for i in range(1, len(array)):
        tail.next = Node(array[i])
        tail = tail.next
    return head


def random_linked_list(
    min_size: int,
    max_size: int,
    min_value: int,
    max_value: int,
    remove_duplicate: bool = False
):
    array = random_array(min_size, max_size, min_value, max_value, remove_duplicate)
    return array_to_linked_list(array)


def random_double_linked_list(
    min_size: int,
    max_size: int,
    min_value: int,
    max_value: int,
    remove_duplicate: bool = False
):
    array = random_array(min_size, max_size, min_value, max_value, remove_duplicate)
    if not array:
        return None

    head = DoubleNode(array[0])
    tail = head
    for i in range(1, len(array)):
        tail.next = DoubleNode(array[i])
        tail.next.prev = tail
        tail = tail.next
    return head


def copy_linked_list(head: Node) -> Node:
    if not head:
        return None

    exist = set()
    new_head = Node(head.val)
    new_tail = new_head
    head = head.next
    while head:
        if head in exist:
            raise Exception("Circular linked list!")
        exist.add(head)
        new_tail.next = Node(head.val)
        new_tail = new_tail.next
        head = head.next
    return new_head


def copy_double_linked_list(head: DoubleNode) -> DoubleNode:
    if not head:
        return None

    exist = set()
    new_head = DoubleNode(head.val)
    new_tail = new_head
    head = head.next
    while head:
        if head in exist:
            raise Exception("Circular linked list!")
        exist.add(head)
        new_tail.next = DoubleNode(head.val)
        new_tail.next.prev = new_tail
        new_tail = new_tail.next
        head = head.next
    return new_head


def linked_list_to_string(head, sep: str = " -> ") -> str:
    s = ""
    exist = set()
    while head:
        if head in exist:
            raise Exception("Circular linked list!")
        exist.add(head)
        s += str(head.val) + sep
        head = head.next
    return s[:-len(sep)]


def double_linked_list_to_string(head, sep: str = " <=> ") -> str:
    s = ""
    exist = set()
    prev = None
    while head:
        assert head.prev == prev, "Double linked list is broken!"
        if head in exist:
            raise Exception("Circular linked list!")
        exist.add(head)
        s += str(head.val) + sep
        prev = head
        head = head.next

    return s[:-len(sep)]


if __name__ == "__main__":
    head = random_linked_list(1, 10, 0, 1000, True)
    print(linked_list_to_string(head))
