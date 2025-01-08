#!/usr/bin/env python

import textwrap
from typing import Any, Callable, Self


type TransformFunc[T] = Callable[[Node[T]], None]
type VisitFunc[T] = Callable[[Node[T]], Any]
type AggrFunc = Callable[[Any, Any, Any], Any]


class Node[T]:
    _left: Self | None
    _right: Self | None
    _data: T

    def __init__(self, data: T):
        self._left = None
        self._right = None
        self._data = data

    @property
    def left(self) -> Self | None:
        return self._left

    @left.setter
    def left(self, left: Self) -> None:
        self._left = left

    @property
    def right(self) -> Self | None:
        return self._right

    @right.setter
    def right(self, right: Self) -> None:
        self._right = right

    @property
    def data(self) -> T:
        return self._data

    @data.setter
    def data(self, data: T) -> None:
        self._data = data

    @property
    def is_leaf(self) -> bool:
        return not (self.has_left or self.has_right)

    @property
    def has_left(self) -> bool:
        return self._left is not None

    @property
    def has_right(self) -> bool:
        return self._right is not None

    @property
    def nr_descendants(self) -> int:
        count = 0
        if self._left is not None:
            count += 1 + self._left.nr_descendants
        if self._right is not None:
            count += 1 + self._right.nr_descendants
        return count

    def transformn(self, func: TransformFunc[T]) -> None:
        func(self)
        if self._left is not None:
            self._left.transformn(func)
        if self._right is not None:
            self._right.transformn(func)

    def __str__(self) -> str:
        return f"{self.data}"

    def __repr__(self) -> str:
        return f"{self.data}"

    def visit(self, visit_func: VisitFunc[T], aggr_func: AggrFunc) -> Any:
        self_value = visit_func(self)
        left_value = (
            self._left.visit(visit_func, aggr_func)
            if self._left is not None
            else None
        )
        right_value = (
            self._right.visit(visit_func, aggr_func)
            if self._right is not None
            else None
        )
        return aggr_func(self_value, left_value, right_value)


def str_visit[T](node: Node[T]) -> str:
    return str(node.data)


def str_aggr(self_value: str, left_value: str, right_value: str) -> str:
    indent = "  "
    aggr = self_value
    if left_value is not None:
        aggr += "\n" + textwrap.indent(left_value, indent)
    if right_value is not None:
        aggr += "\n" + textwrap.indent(right_value, indent)
    return aggr


def double_value(node: Node[int]) -> None:
    node.data = 2 * node.data


class Tree[T]:
    _root: Node[T] | None

    def __init__(self, root: Node[T] | None = None):
        self._root = root

    @property
    def root(self) -> Node[T] | None:
        return self._root

    @root.setter
    def root(self, root: Node[T]) -> None:
        self._root = root

    @property
    def nr_of_nodes(self) -> int:
        return 0 if self._root is None else 1 + self._root.nr_descendants

    def transformn(self, func: TransformFunc[T]) -> None:
        if self._root is not None:
            self._root.transformn(func)

    def __str__(self) -> str:
        return (
            ""
            if self._root is None
            else self._root.visit(str_visit, str_aggr)
        )

    def __repr__(self) -> str:
        return f"{self._root}"


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    tree = Tree(root)
    print(tree)
    print(f"number of nodes = {tree.nr_of_nodes}")
    tree.transformn(double_value)
    print(tree)
