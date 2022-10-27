
from typing import Any

class Node:
    value: Any
    next: 'Node'
    def __init__(self, value: Any)->None:
        self.value=value

class LinkedList:
    head: Node
    tail: Node
    def __init__(self)->None:
        self.head = None
        self.tail = None
        
    def push(self,element: Any)->None:
        node = Node(element)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.tail
            self.head = node

    def append(self,element):
        lastnode = Node(element)
        lastnode.next = None
        self.tail = lastnode

    def len(self):
        node=self.head
        len=0

        while node is not None:
            len=len+1
            node=node.next
        return len

    def remove_last(self):
        element = self.tai
         i=0

        while(i<after):
            currentNode=currentNode.next
            i=i+1

        currentNode.next=currentNode.next.next
  
    def print(self)->None:
        node=self.head

        while node is not None:
            print(node.value,"-> ", end="")
            node=node.next
        print("None")
list_=LinkedList()
list_.append(3)
list_.append(4)
list_.push(5)
#print(list_.NodePos(0))
list_.print()
list_.insertNode(8,1)
list_.print()
print(list_.pop())
print(list_.removeLast())
list_.print()
list_.append(6)
list_.append(10)
list_.print()
list_.remove(1)
list_.print()
print(list_.len())
#LIFO

class Node:
    def __init__(self, value=None, next=None):
        self.value=value
        self.next=next

class Stack:
    def __init__(self,top=None):
        self._storage=top
        self.size=0

    def push(self, element:any):
        node=Node(element)

        if self._storage is None:
            self._storage=node
            self.size = self.size + 1
            return

        temp=self._storage
        self._storage=node
        node.next=temp
        self.size=self.size+1

    def pop(self):
        if self._storage is None:
            print("nie mozna pop, stack jest pusty")
            return

        value=self._storage

        self._storage=self._storage.next
        self.size = self.size - 1

        return value

    def __len__(self):
        return self.size

    def print(self):
        node = self._storage

        while node is not None:
            print(node.value)
            node = node.next


stack=Stack()
stack.push(10)
stack.push(11)
stack.push(12)
stack.print()
print("-------------")
stack.pop()
stack.print()
print(len(stack))
