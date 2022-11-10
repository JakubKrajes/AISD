from typing import Any
import graphviz



class TreeNode:
    value: Any
    children: List["TreeNode"]

    def __init__(self, value):
        self.value = value
        self.children = []

    def is_leaf(self) -> bool:
        if self.children is None:
            return True

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)
