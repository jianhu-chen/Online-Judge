# -*- coding: utf-8 -*-
import json
import random
import unittest
from typing import Any, Set, List, Mapping


class Node:

    def __init__(self, val: Any) -> None:
        self.val = val
        self.indegree: int = 0  # 入度, 自动维护
        self.outdegree: int = 0  # 出度, 自动维护
        self.nexts: List[Node] = []
        self.edges: List[Edge] = []

    def __repr__(self) -> str:
        return "Node(" + str(self.val) + ")"

    @property
    def nexts(self) -> List['Node']:
        return self._nexts

    __str__ = __repr__


class Edge:

    def __init__(self, weight: float, src: Node, des: Node) -> None:
        self.weight: float = weight
        self.src: Node = src
        self.des: Node = des

    def __repr__(self) -> str:
        return f"Edge(weight={self.weight}, src={self.src}, des={self.des})"

    __str__ = __repr__


class JsonEncoder(json.JSONEncoder):

    def default(self, field):

        if isinstance(field, set):
            return list(field)
        elif isinstance(field, Node):
            return str(field)
        elif isinstance(field, Edge):
            return str(field)
        else:
            return json.JSONEncoder.default(self, field)


class Graph:

    def __init__(self, nodes: Mapping[Any, Node], edges: Set[Edge]) -> None:
        self.nodes: Mapping[Any, Node] = nodes
        self.edges: Set = edges

    def __repr__(self) -> str:
        ans = "Graph(nodes="
        ans += json.dumps(self.nodes, indent=2, cls=JsonEncoder)
        ans += ", edges="
        ans += json.dumps(self.edges, indent=2, cls=JsonEncoder)
        ans += ")"
        return ans


class LinkedListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "Node(val={})".format(self.val)

    __str__ = __repr__


def adjacency_list_to_graph(adjacency_list: List[LinkedListNode]):
    """Convert adjacency list to graph."""
    nodes = {}
    edges = set()
    for pre in adjacency_list:
        if not pre:
            raise ValueError("Invalid adjacency list")
        # for the first node, create a node
        if pre.val not in nodes:
            pre_node = Node(pre.val)
        else:
            pre_node = nodes[pre.val]
        nodes[pre.val] = pre_node
        # for the rest of the nodes, add edges
        cur = pre.next
        while cur:
            if cur.val not in nodes:
                cur_node = Node(cur.val)
            else:
                cur_node = nodes[cur.val]
            # update node degree
            pre_node.outdegree += 1
            cur_node.indegree += 1
            # update node nexts
            pre_node.nexts.append(cur_node)
            # new edge
            pre_cur_edge = Edge(1, pre_node, cur_node)
            # update node edges
            pre_node.edges.append(pre_cur_edge)
            # insert to graph nodes
            nodes[cur.val] = cur_node
            # insert to graph edges
            edges.add(pre_cur_edge)
            cur = cur.next
    return Graph(nodes, edges)


def adjacency_matrix_to_graph(adjacency_matrix):
    """Convert adjacency matrix to graph."""
    assert len(adjacency_matrix) == len(adjacency_matrix[0])
    n = len(adjacency_matrix)
    nodes = {i: Node(i) for i in range(n)}
    edges = set()
    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j] != 0:
                edge = Edge(adjacency_matrix[i][j], nodes[i], nodes[j])
                edges.add(edge)
                nodes[i].outdegree += 1
                nodes[j].indegree += 1
                nodes[i].nexts.append(nodes[j])
                nodes[i].edges.append(edge)

    return Graph(nodes, edges)


def random_graph(
    min_nodes: int = 1,
    max_nodes: int = 10,
    weight_range: tuple = (1, 10),
    directed: bool = False,
    edge_prob: float = 0.5,
):
    """Generate a random graph."""
    num_nodes = random.randint(min_nodes, max_nodes)
    matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                continue
            weight = random.randint(*weight_range)
            matrix[i][j] = weight if random.random() < edge_prob else 0

    if not directed:
        for i in range(num_nodes):
            for j in range(i, num_nodes):
                matrix[i][j] = matrix[j][i]

    # avoid independent nodes
    for i in range(num_nodes):
        if set(matrix[i][i + 1:]) == {0}:
            j = random.randint(i + 1, num_nodes - 1)
            matrix[i][j] = random.randint(*weight_range)
            if not directed:
                matrix[j][i] = matrix[i][j]

    return adjacency_matrix_to_graph(matrix)


class Tester(unittest.TestCase):

    def test_adjacency_list_to_graph():
        # fake data
        node0 = LinkedListNode(0)
        node1 = LinkedListNode(1)
        node2 = LinkedListNode(2)
        node3 = LinkedListNode(3)
        node4 = LinkedListNode(4)
        node5 = LinkedListNode(5)

        adjacency_list = []
