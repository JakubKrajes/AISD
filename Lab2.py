from typing import Any


class Node:
    value: Any
    next: 'Node'


def __init__(self, value: int, next: Node) -> None:
    self.value = value
    self.next = Node


class LinkedList:
    head: Node
    tail: Node


def __init__(self, head: None, tail: None) -> None:
    self.head = head
    self.tail = tail
    self.list = []

# push(self, value: Any) -> None:

# append(self, value: Any) -> None:

# node(self, at: int) -> Node:

# insert(self, value: Any, after: Node) -> None:

# metoda pop(self) -> Any:

# remove_last(self) -> Any

# remove(self, after: Node) -> Any

# print

# len
    def __str__(self):
        return self.list

list_ = LinkedList()

print(list_)
assert list_.head == None
