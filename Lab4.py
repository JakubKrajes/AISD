from typing import Any, List


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self) -> str:
        return str(self.value)

    def min(self) -> 'BinaryNode':
        if self.left_child > self.right_child:
            print("To nie jest BST")
        elif self.left_child is not None:
            return self.left_child.min()
        return self


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, value):
        self.root = BinaryNode(value)

    def insert(self, value: Any) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node is None:
            return BinaryNode(value)
        if value < node.value:
            node.left_child = self._insert(node.left_child, value)
        if value >= node.value:
            node.right_child = self._insert(node.right_child, value)

        return node
